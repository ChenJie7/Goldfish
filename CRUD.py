"""
-------------------------------------------------------------------
This is a Goldfish Project File

Authors: Max Witwer, Jie Chen, Elliot Cole
Collaboration with the Baker Lab

This file was generated during an internship at the institute for
protein design

Description:
This file contains all functions that allow for database CRUD 
opperations. It loads the url from a saved envirnomental variable
containing the location for the running MongoDB database. It then
specifies a number of functions that allow for querying, adding 
and updating data contained in the various collections within
the database.


Date: 07/06/2024
-------------------------------------------------------------------
"""

from dotenv import load_dotenv
import os

from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

# Append the path to the schemas directory
import sys
sys.path.append("./db_schemas")

from graph_map import GraphMap
from process_step import ProcessStep

# load environmental varibles from ".env" file
load_dotenv()

# connect to database and create database objs

database_url = os.getenv('DATABASE_URL')
client = MongoClient(database_url)

db = client.Goldfish
graph_collection = db.graph_map
process_collection = db.process_step


# Read Graph Data 

def pull_graph_id(ID:str):
	"""
	Pull a graph document by its ID.

	:param ID: The ID of the graph document to retrieve.
	:return: The graph document if found, otherwise None.
	"""
	result = graph_collection.find_one({"_id" : ID})
	if result:
		return result

def pull_graph_project_name(name:str):
	"""
	Pull a graph document by its project name.

	:param name: The project name of the graph document to retrieve.
	:return: The graph document if found, otherwise None.
	"""
	result = graph_collection.find_one({"project_name" : name})
	if result:
		return result

def pull_graphs_owner(owner:str):
	"""
	Pull all graph documents by the owner's name.

	:param owner: The name of the owner.
	:return: A list of graph documents owned by the specified owner.
	"""
	result = list(graph_collection.find({"owner" : owner}))
	if result:
		return result

def pull_graphs_email(email:str):
	"""
	Pull all graph documents by the owner's email.

	:param email: The email of the owner.
	:return: A list of graph documents owned by the specified email.
	"""
	result = list(graph_collection.find({"owner_email" : email}))
	if result:
		return result


# Read Process Data 

def pull_process_id(ID:str):
	"""
	Pull a process document by its ID.

	:param ID: The ID of the process document to retrieve.
	:return: The process document if found, otherwise None.
	"""
	result = process_collection.find_one({"_id" : ID})
	if result:
		return result

def pull_processes_parent_graph(parent_graph:str):
	result = list(process_collection.find({"parent_graph" : parent_graph}))
	if result:
		return result

def pull_processes_data_type(data_key:str):
	"""
	Pull all process documents that contain a specific key in the elastic_data_paths dictionary.

	:param data_key: The key to search for in the elastic_data_paths dictionary.
	:return: A list of process documents that contain the specified key.
	"""
	query = {
		f"elastic_data_paths.{data_key}": {"$exists": True}
	}
	print(query)
	result = list(process_collection.find(query))

	if result:
		return result









