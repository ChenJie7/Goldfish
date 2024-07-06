from dotenv import load_dotenv
import os


from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

import sys
sys.path.append("./db_schemas")

from graph_map import GraphMap
from process_step import ProcessStep

load_dotenv()

database_url = os.getenv('DATABASE_URL')