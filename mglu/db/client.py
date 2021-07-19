import logging
from contextlib import contextmanager

from .. import settings
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import Session

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


# Session = sessionmaker(bind=client.engine)
class MsgScheduleClient(SQLClient):
    def __init__(self) -> None:

        super().__init__()

    @contextmanager
    def get_session(self):
        session = Session(self.engine)
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def post(self, args):
        with self.get_session() as session:
            new = MsgSchedules(**args)
            session.add(new)
            session.commit()
            return {"id": new.id}

    def delete(self, id):
        stmt = delete(MsgSchedules).where(MsgSchedules.id == id)

        with self.get_session() as session:
            session.execute(stmt)

            return {"id": id}

    def get(self, id):
        with self.get_session() as session:
            result = session.query(MsgSchedules).filter(MsgSchedules.id == id).first()
            return {
                "id": result.id,
                "scheduled_date": str(result.scheduled_date),
                "type": result.type,
                "destination": result.destination,
                "message": result.message,
                "status": result.status,
            }

    def paginated(self, page, per_page):
        with self.get_session() as session:
            return (
                session.query(MsgSchedules)
                .offset(page * per_page)
                .limit(per_page)
                .all()
            )

    def filter(self, args):
        with self.get_session() as session:
            return session.query(MsgSchedules).filter_by(**args).all()


client = MsgScheduleClient()
client.create_engine()
