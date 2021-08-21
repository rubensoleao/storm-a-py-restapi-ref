from storm.db.client import SQLClient


client = SQLClient()
client.create_engine()
client.create_tables()
