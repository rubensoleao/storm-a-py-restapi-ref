from mglu.db.client import SQLClient


def init_tables():
    client = SQLClient()
    client.create_engine()
    client.create_tables()
