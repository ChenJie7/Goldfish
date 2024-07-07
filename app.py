"""
-------------------------------------------------------------------
This is a Goldfish Project File

Authors: Max Witwer, Jie Chen, Elliot Cole
Collaboration with the Baker Lab

This file was generated during an internship at the institute for
protein design

Description:
This file contains all FastAPI endpoints that allow for querying 
the database. It provides read operations for graph and process 
collections within the MongoDB database, enabling CRUD functionality 
via HTTP requests. The endpoints are categorized for better 
documentation and ease of use.

Date: 07/06/2024
-------------------------------------------------------------------
"""

from fastapi import FastAPI, HTTPException
from CRUD import *

# meta data for autodocumentation
tags_metadata = [
    {
        "name": "Graph Read Operation",
        "description": "Endpoints that relate to reading from the graph collection",
    },
    {
        "name": "Process Read Operations",
        "description": "Endpoints that relate to reading from the process collection",
    }
]

# generate app instance
app = FastAPI()

@app.get("/CRUD/read/graph_id/{item_id}", tags=["Graph Read Operation"])
async def read_graph_data_from_id(item_id: str):
    """
    Endpoint to read graph data by ID.
    
    :param item_id: The ID of the graph document to retrieve.
    :return: The graph document if found, otherwise raises a 404 HTTP exception.
    """
    result = pull_graph_id(item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Graph not found")
    return {"result": result}

@app.get("/CRUD/read/graph_name/{project_name}", tags=["Graph Read Operation"])
async def read_graph_data_from_project_name(project_name: str):
    """
    Endpoint to read graph data by project name.
    
    :param project_name: The project name of the graph document to retrieve.
    :return: The graph document if found, otherwise raises a 404 HTTP exception.
    """
    result = pull_graph_project_name(project_name)
    if not result:
        raise HTTPException(status_code=404, detail="Graph not found")
    return {"result": result}

@app.get("/CRUD/read/graph_owner/{owner}", tags=["Graph Read Operation"])
async def read_graph_data_from_owner(owner: str):
    """
    Endpoint to read graph data by owner's name.
    
    :param owner: The name of the owner.
    :return: A list of graph documents owned by the specified owner, otherwise raises a 404 HTTP exception.
    """
    result = pull_graphs_owner(owner)
    if not result:
        raise HTTPException(status_code=404, detail="Graphs not found")
    return {"result": result}

@app.get("/CRUD/read/graph_email/{email}", tags=["Graph Read Operation"])
async def read_graph_data_from_email(email: str):
    """
    Endpoint to read graph data by owner's email.
    
    :param email: The email of the owner.
    :return: A list of graph documents owned by the specified email, otherwise raises a 404 HTTP exception.
    """
    result = pull_graphs_email(email)
    if not result:
        raise HTTPException(status_code=404, detail="Graphs not found")
    return {"result": result}

@app.get("/CRUD/read/process_id/{id}", tags=["Process Read Operations"])
async def read_process_data_from_id(id: str):
    """
    Endpoint to read process data by ID.
    
    :param id: The ID of the process document to retrieve.
    :return: The process document if found, otherwise raises a 404 HTTP exception.
    """
    result = pull_process_id(id)
    if not result:
        raise HTTPException(status_code=404, detail="Process not found")
    return {"result": result}

@app.get("/CRUD/read/process_parent/{parent_graph}", tags=["Process Read Operations"])
async def read_process_data_from_parent_graph(parent_graph: str):
    """
    Endpoint to read process data by parent graph ID.
    
    :param parent_graph: The ID of the parent graph.
    :return: A list of process documents associated with the specified parent graph, otherwise raises a 404 HTTP exception.
    """
    result = pull_processes_parent_graph(parent_graph)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}

@app.get("/CRUD/read/process_data_type/{data_key}", tags=["Process Read Operations"])
async def read_process_data_from_meta_data_tag(data_key: str):
    """
    Endpoint to read process data by a specific key in the elastic_data_paths dictionary.
    
    :param data_key: The key to search for in the elastic_data_paths dictionary.
    :return: A list of process documents that contain the specified key, otherwise raises a 404 HTTP exception.
    """
    result = pull_processes_data_type(data_key)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}