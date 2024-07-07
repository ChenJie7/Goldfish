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
import json

# meta data for autodocumentation
tags_metadata = [
    {
        "name": "Graph Read Operations",
        "description": "Endpoints that relate to reading from the graph collection",
    },
    {
        "name": "Process Read Operations",
        "description": "Endpoints that relate to reading from the process collection",
    }
]

# generate app instance
app = FastAPI()

@app.get("/CRUD/read/graph_instance/{filter}", tags=["Graph Read Operations"])
async def read_graph_instance(filter: str):
    """
    search database and return specific match to input filter

    **Parameters:**
    - **filter**: Filter to be applied to the data.

    **Returns:**
    - A graph document if found, otherwise raises a 404 HTTP exception.
    """
    
    result = pull_graph_instance(json.loads(filter))
    if not result:
        raise HTTPException(status_code=404, detail="Graph not found")
    return {"result": result}

@app.get("/CRUD/read/graph_collection/{filter}", tags=["Graph Read Operations"])
async def read_graph_collection(filter: str):
    """
    search entire database and return all found matches to the filter

    **Parameters:**
    - **filter**: Filter to be applied to the data.

    **Returns:**
    - A list of graph documents if found, otherwise raises a 404 HTTP exception.
    """
    
    result = pull_graph_collection(json.loads(filter))
    if not result:
        raise HTTPException(status_code=404, detail="Graph not found")
    return {"result": result}



@app.get("/CRUD/read/process_instance/{filter}", tags=["Process Read Operations"])
async def read_process_instance(filter: str):
    """
    search database and return specific match to input filter

    **Parameters:**
    - **filter**: Filter to be applied to the data.

    **Returns:**
    - A graph document if found, otherwise raises a 404 HTTP exception.
    """
    
    result = pull_process_instance(json.loads(filter))
    if not result:
        raise HTTPException(status_code=404, detail="Process not found")
    return {"result": result}

@app.get("/CRUD/read/process_collection/{filter}", tags=["Process Read Operations"])
async def read_process_collection(filter: str):
    """
    search entire database and return all found matches to the filter

    **Parameters:**
    - **filter**: Filter to be applied to the data.

    **Returns:**
    - A list of graph documents if found, otherwise raises a 404 HTTP exception.
    """
    result = pull_process_collection(json.loads(filter))
    if not result:
        raise HTTPException(status_code=404, detail="Graph not found")
    return {"result": result}