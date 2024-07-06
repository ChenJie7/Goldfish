from fastapi import FastAPI

from CRUD import *

load_dotenv()

database_url = os.getenv('DATABASE_URL')

client = MongoClient(database_url)
client = MongoClient(cluster)

db = client.Goldfish
graph_collection = db.graph_map
process_collection = db.process_map


# @app.post("/CRUD/add_graph", tags=["Translation"])
# async def add_graph():


