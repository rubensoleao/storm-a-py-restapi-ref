import logging

import mglu.settings as settings
from sqlalchemy import create_engine

from .models import Base


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

    def get_connection(self):
        return self.engine.connect()
