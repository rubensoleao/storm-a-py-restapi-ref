import logging
from contextlib import contextmanager
from copy import Error

from sqlalchemy import create_engine, delete
from sqlalchemy.orm import Session, query

from .. import settings
from .models import Base, MsgSchedules


class SQLClient:
    def __init__(self) -> None:
        self.engine = None

    def create_engine(self):
        mysql_uri = f"mysql+pymysql://{settings.db_user}:{settings.db_password}@{settings.db_server}:{settings.db_port}/{settings.db_name}"
        try:
            self.engine = create_engine(mysql_uri)
        except Exception as e:
            logging.critical("Coudn't connect to database")
            logging.critical(e)
            raise e from e

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    @property
    def connection(self):
        return self.engine.connect()


class MsgScheduleClient(SQLClient):
    """Client that handles requests to DB for message scheduling events"""

    def __init__(self) -> None:

        super().__init__()

    @contextmanager
    def get_session(self):
        session = Session(self.engine)
        try:
            yield session
            session.commit()
        except Error as e:
            session.rollback()
            raise e from e
        finally:
            session.close()

    def post(self, args):
        with self.get_session() as session:
            new = MsgSchedules(**args)
            session.add(new)
            session.commit()
            return {"id": new.id}

    def delete(self, id):
        with self.get_session() as session:
            stmt = delete(MsgSchedules).where(MsgSchedules.id == id)
            session.execute(stmt)

            return {"id": id}

    def get(self, args, page, limit):
        with self.get_session() as session:
            query = session.query(MsgSchedules).filter_by(**args)
            count = query.count()
            query = query.offset(page - 1 * limit).limit(limit)
            data = [item.__dict__ for item in query.all()]
            for item in data:
                del item["_sa_instance_state"]
                del item["created"]
                item["scheduled_date"] = str(item["scheduled_date"])
            return {"data": data, "total": count, "page": page}


client = MsgScheduleClient()
client.create_engine()
