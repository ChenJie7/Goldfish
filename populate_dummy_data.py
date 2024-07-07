"""
-------------------------------------------------------------------
This is a Goldfish Project File

Authors: Max Witwer, Jie Chen, Elliot Cole
Collaboration with the Baker Lab

This file was generated during an internship at the institute for
protein design

Description:
This file contains a system to load some dummy data onto the 
database inorder to develop and test the system

Date: 07/06/2024
-------------------------------------------------------------------
"""

from dotenv import load_dotenv
import os

from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

# Add the path to the schemas directory to the system path
import sys
sys.path.append("./db_schemas")


# Import schema classes
from graph_map import GraphMap
from process_step import ProcessStep

# Load environmental variables from the ".env" file
load_dotenv()


# Generate some object ids
graph_map_ID = str(ObjectId())
process_step_IDs = [str(ObjectId()) for _ in range(10)]

# generate timestamp
time_stamp = datetime.now()

# Create an example graph_map instance
example_graph_inst = {
    "_id": graph_map_ID,
    "project_name": "Example Schema",
    "process_list": process_step_IDs,
    "process_meta_data": {"description": "variable meta data goes here"},
    "owner": "Max Witwer",
    "owner_email": "mwitwer@uw.edu",
    "date_created": time_stamp,
    "date_updated": time_stamp
}

# Create a list of example process_step instances
example_process_inst = [{
    "_id": process_step_IDs[i],
    "parent_graph": graph_map_ID,
    "meta_data": {"description": "variable meta data goes here"},
    "elastic_data_paths": {
        "pdb": ["/some_path1.pdb", "/some_path2.pdb", "/some_path3.pdb"]
    },
    "file_location_type": "digs_local",
    "date_created": time_stamp,
    "date_updated": time_stamp
} for i in range(len(process_step_IDs))]

# Create GraphMap and ProcessStep objects using the example instances
graph_map = GraphMap(**example_graph_inst)
process_steps = [ProcessStep(**process) for process in example_process_inst]

# pull environmental variable and connect to database
database_url = os.getenv('DATABASE_URL')
client = MongoClient(database_url)

# generate database objects
db = client.Goldfish
graph_collection = db.graph_map
process_collection = db.process_step




# push data to database
graph_collection.insert_one(graph_map.dict())
process_collection.insert_many([process.dict() for process in process_steps])
