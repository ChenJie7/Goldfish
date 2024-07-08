"""
-------------------------------------------------------------------
This is a Goldfish Project File

Authors: Max Witwer, Jie Chen, Elliott Cole
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
from crud_models import *

# load environmental varibles from ".env" file
load_dotenv()

# connect to database and create database objs

database_url = os.getenv('DATABASE_URL')
client = MongoClient(database_url)

db = client.Goldfish
graph_collection = db.graph_map
process_collection = db.process_step


# Read Graph Data 

def pull_graph_instance(filter):
	"""
	Pull a specific document with specific filter.

	:param filter: filter to apply to database.
	:return: The graph document if found, otherwise None.
	"""
	return graph_collection.find_one(filter)

def pull_graph_collection(filter):
	"""
	Pull a collection of graphs under specific filter.

	:param filter: filter to apply to database.
	:return: The graph document if found, otherwise None.
	"""
	return list(graph_collection.find(filter))

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

# Update Graph Data 

def update_graph_process_meta_data(update_id:str, process_meta_data:dict):
	"""
	Update the process metadata of a graph document.

	:param update_id: The unique identifier of the graph document to update.
	:param process_meta_data: The process metadata to update in the graph document.
	:return: A message indicating the outcome of the update operation.
	"""
	# generate timestamp
	time_stamp = datetime.now()

	# update database
	result = graph_collection.update_one(
			{"_id":update_id}, 
			{'$set': {
				"process_meta_data":process_meta_data,
				"date_updated":time_stamp
			}}
		)

	if result.modified_count > 0:
		return f"item '{update_id}' modified with supplied meta data"

def update_graph_project_name(update_id:str, project_name:str):
	"""
	Update the project name of a graph document.

	:param update_id: The unique identifier of the graph document to update.
	:param project_name: The new project name to update in the graph document.
	:return: A message indicating the outcome of the update operation.
	"""
	# generate timestamp
	time_stamp = datetime.now()

	# update database
	result = graph_collection.update_one(
			{"_id":update_id}, 
			{'$set': {
				"project_name":project_name,
				"date_updated":time_stamp
			}}
		)

	if result.modified_count > 0:
		return f"item '{update_id}' modified with supplied meta data"

def update_graph_owner_email(update_id:str, owner_email:str):
	"""
	Update the owner email of a graph document.

	:param update_id: The unique identifier of the graph document to update.
	:param owner_email: The new owner email to update in the graph document.
	:return: A message indicating the outcome of the update operation.
	"""
	# generate timestamp
	time_stamp = datetime.now()

	# update database
	result = graph_collection.update_one(
			{"_id":update_id}, 
			{'$set': {
				"owner_email":owner_email,
				"date_updated":time_stamp
			}}
		)

	if result.modified_count > 0:
		return f"item '{update_id}' modified with supplied meta data"

def update_graph_owner(update_id:str, owner:str):
	"""
	Update the owner of a graph document.

	:param update_id: The unique identifier of the graph document to update.
	:param owner: The new owner to update in the graph document.
	:return: A message indicating the outcome of the update operation.
	"""
	# generate timestamp
	time_stamp = datetime.now()

	# update database
	result = graph_collection.update_one(
			{"_id":update_id}, 
			{'$set': {
				"owner":owner,
				"date_updated":time_stamp
			}}
		)

	if result.modified_count > 0:
		return f"item '{update_id}' modified with supplied meta data"


# Delete Graph Data 

def delete_graph(id:str):
	"""
	Delete a graph document by its unique identifier and 
	all associated process documents.

	:param id: The unique identifier of the graph document to delete.
	:return: A message indicating the outcome of the deletion operation, 
	         including associated processes.
	"""
	# Delete the graph document with the specified id
	graph_result = graph_collection.delete_one({"_id" : f"{id}"})

	# Delete all process documents associated with the specified graph id
	process_result = delete_all_from_parent_graph(id)

	# Validate results
	if graph_result.deleted_count > 0 and process_result:
		return f"item '{id}' and all associated processes deleted"


# Create Graph Data 


# Read Process Data 

def pull_process_instance(filter):
	"""
	Pull a specific document with specific filter.

	:param filter: filter to apply to database.
	:return: The graph document if found, otherwise None.
	"""
	return process_collection.find_one(filter)

def pull_process_collection(filter):
	"""
	Pull a collection of graphs under specific filter.

	:param filter: filter to apply to database.
	:return: The graph document if found, otherwise None.
	"""
	return list(process_collection.find(filter))

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
	"""
	Pull all process documents that derive from the parent graph.

	:param data_key: The ID to the parent graph.
	:return: A list of process documents that contain the specified parent.
	"""
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

def pull_processes_file_location_type(file_location_type:str):
	"""
	Pull all process data contained in a catigory of file location

	:param file_location: process location type (embedded, digs_local, pool).
	:return: A list of process documents stored in a storage catigory.
	"""
	result = list(process_collection.find({"file_location_type" : file_location_type}))
	if result:
		return result


# Update Process Data 

def update_process_meta_data(update_id:str, meta_data:dict):
	"""
	Update the metadata of a process document.

	:param update_id: The unique identifier of the process document to update.
	:param meta_data: The metadata to update in the process document.
	:return: A message indicating the outcome of the update operation.
	"""
	# generate timestamp
	time_stamp = datetime.now()

	# update database
	result = process_collection.update_one(
			{"_id":update_id}, 
			{'$set': {
				"meta_data":meta_data,
				"date_updated":time_stamp
			}}
		)

	if result.modified_count > 0:
		return f"item '{update_id}' modified with supplied meta data"

def update_process_elastic_data_paths(update_id:str, elastic_data_paths:dict):
	"""
	Update the elastic data paths of a process document.

	:param update_id: The unique identifier of the process document to update.
	:param elastic_data_paths: The elastic data paths to update in the process document.
	:return: A message indicating the outcome of the update operation.
	"""
	# generate timestamp
	time_stamp = datetime.now()

	# update database
	result = process_collection.update_one(
			{"_id":update_id}, 
			{'$set': {
				"elastic_data_paths":elastic_data_paths,
				"date_updated":time_stamp
			}}
		)

	if result.modified_count > 0:
		return f"item '{update_id}' modified with supplied meta data"

def update_process_file_location_type(update_id:str, file_location_type:str):
	"""
	Update the file location type of a process document.

	:param update_id: The unique identifier of the process document to update.
	:param file_location_type: The file location type to update in the process document.
	:return: A message indicating the outcome of the update operation.
	"""
	# generate timestamp
	time_stamp = datetime.now()

	# update database
	result = process_collection.update_one(
			{"_id":update_id}, 
			{'$set': {
				"file_location_type":file_location_type,
				"date_updated":time_stamp
			}}
		)

	if result.modified_count > 0:
		return f"item '{update_id}' modified with supplied meta data"

# Delete Process Data 

def delete_process(id:str):
	"""
	Delete a process document by its unique identifier and remove it from
	parent list

	:param id: The unique identifier of the process document to delete.
	:return: A message indicating the outcome of the deletion operation.
	"""
	# generate timestamp
	time_stamp = datetime.now()

	# find parent list and remove this id from parent if it exists
	process_data = pull_process_id(id)
	if process_data:
		parent_graph_data = pull_graph_id(process_data["parent_graph"])
		process_list = parent_graph_data["process_list"]
		process_list.remove(id)
		list_modified_result = graph_collection.update_one(
				{"_id":process_data["parent_graph"]}, 
				{'$set': {
					"process_list":process_list,
					"date_updated":time_stamp
				}}
			)

	result = process_collection.delete_one({"_id" : f"{id}"})
	if result.deleted_count > 0 and list_modified_result.modified_count > 0:
		return f"item '{id}' deleted"

def delete_all_from_parent_graph(parent_graph:str):
	"""
	Delete all process documents associated with a specific parent graph.

	:param parent_graph: The identifier of the parent graph whose associated process documents will be deleted.
	:return: A message indicating the outcome of the deletion operation.
	"""
	result = process_collection.delete_many({"parent_graph" : f"{parent_graph}"})
	if result.deleted_count > 0:
		return f"items under '{parent_graph}' graph deleted"


# Create Process Data 






