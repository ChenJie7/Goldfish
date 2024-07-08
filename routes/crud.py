"""
-------------------------------------------------------------------
This is a Goldfish Project File

Authors: Max Witwer, Jie Chen, Elliott Cole
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

# routes.py
from fastapi import APIRouter, HTTPException
from CRUD_utils import *
import json

from crud_models import *

import uuid

crud_router = APIRouter()

@crud_router.post("/CRUD/read/graph_instance/", tags=["General Graph Read Operations"])
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

@crud_router.post("/CRUD/read/graph_collection/", tags=["General Graph Read Operations"])
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

@crud_router.get("/CRUD/read/graph_id/{item_id}", tags=["Specific Graph Read Operations"])
async def read_graph_data_from_id(item_id: str):
    """
    Endpoint to read graph data by ID.

    **Parameters:**
    - **item_id**: The ID of the graph document to retrieve.

    **Returns:**
    - The graph document if found, otherwise raises a 404 HTTP exception.
    """
    result = pull_graph_id(item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Graph not found")
    return {"result": result}

@crud_router.get("/CRUD/read/graph_name/{project_name}", tags=["Specific Graph Read Operations"])
async def read_graph_data_from_project_name(project_name: str):
    """
    Endpoint to read graph data by owner's name.

    **Parameters:**
    - **owner**: The name of the owner.

    **Returns:**
    - A list of graph documents owned by the specified owner, otherwise raises a 404 HTTP exception.
    """
    result = pull_graph_project_name(project_name)
    if not result:
        raise HTTPException(status_code=404, detail="Graph not found")
    return {"result": result}

@crud_router.get("/CRUD/read/graph_owner/{owner}", tags=["Specific Graph Read Operations"])
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

@crud_router.get("/CRUD/read/graph_email/{email}", tags=["Specific Graph Read Operations"])
async def read_graph_data_from_email(email: str):
    """
    Endpoint to read graph data by owner's email.

    **Parameters:**
    - **email**: The email of the owner.

    **Returns:**
    - A list of graph documents owned by the specified email, otherwise raises a 404 HTTP exception.
    """
    result = pull_graphs_email(email)
    if not result:
        raise HTTPException(status_code=404, detail="Graphs not found")
    return {"result": result}

@crud_router.post("/CRUD/read/process_instance/", tags=["General Process Read Operations"])
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

@crud_router.post("/CRUD/read/process_collection/", tags=["General Process Read Operations"])
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

@crud_router.get("/CRUD/read/process_id/{id}", tags=["Specific Process Read Operations"])
async def read_process_data_from_id(id: str):
    """
    Endpoint to read process data by ID.

    **Parameters:**
    - **id**: The ID of the process document to retrieve.

    **Returns:**
    - The process document if found, otherwise raises a 404 HTTP exception.
    """
    result = pull_process_id(id)
    if not result:
        raise HTTPException(status_code=404, detail="Process not found")
    return {"result": result}

@crud_router.get("/CRUD/read/process_parent/{parent_graph}", tags=["Specific Process Read Operations"])
async def read_process_data_from_parent_graph(parent_graph: str):
    """
    Endpoint to read process data by parent graph ID.

    **Parameters:**
    - **parent_graph**: The ID of the parent graph.

    **Returns:**
    - A list of process documents associated with the specified parent graph, otherwise raises a 404 HTTP exception.
    """
    result = pull_processes_parent_graph(parent_graph)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}

@crud_router.get("/CRUD/read/process_data_type/{data_key}", tags=["Specific Process Read Operations"])
async def read_process_data_from_meta_data_tag(data_key: str):
    """
    Endpoint to read process data by a specific key in the elastic_data_paths dictionary.

    **Parameters:**
    - **data_key**: The key to search for in the elastic_data_paths dictionary.

    **Returns:**
    - A list of process documents that contain the specified key, otherwise raises a 404 HTTP exception.
    """
    result = pull_processes_data_type(data_key)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}

@crud_router.get("/CRUD/read/process_file_location_type/{file_location}", tags=["Specific Process Read Operations"])
async def read_process_data_from_file_location_type(file_location_type: str):
    """
    Endpoint to read process data by a specific data location category.

    **Categories include:** 
    - embedded: stored within the data structure itself
    - digs_local: stored on someones digs locally
    - pool: stored in some pooled or standardized

    **Parameters:**
    - **data_key**: The key to search for in the elastic_data_paths dictionary.

    **Returns:**
    - A list of process documents that contain the specified key, otherwise raises a 404 HTTP exception.
    """
    result = pull_processes_file_location_type(file_location_type)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}


@crud_router.get("/CRUD/delete/graph_file_id/{id}", tags=["Specific Graph Delete Operations"])
async def delete_graph_from_id(id: str):
    """
    Endpoint to delete a graph by a specific ID.

    **Parameters:**
    - **id**: The ID of the graph to delete.

    **Returns:**
    - A result indicating the success of the deletion, otherwise raises a 404 HTTP exception.
    """
    result = delete_graph(id)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}    

@crud_router.get("/CRUD/delete/process_file_id/{id}", tags=["Specific Process Delete Operations"])
async def delete_process_from_id(id: str):
    """
    Endpoint to delete a process by a specific ID.

    **Parameters:**
    - **id**: The ID of the process to delete.

    **Returns:**
    - A result indicating the success of the deletion, otherwise raises a 404 HTTP exception.
    """
    result = delete_process(id)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}


@crud_router.get("/CRUD/delete/process_partent_id/{parent_id}", tags=["Specific Process Delete Operations"])
async def delete_processes_from_parent_id(parent_id: str):
    """
    Endpoint to delete processes by a specific parent ID.

    **Parameters:**
    - **parent_id**: The parent ID to delete processes from.

    **Returns:**
    - A result indicating the success of the deletion, otherwise raises a 404 HTTP exception.
    """
    result = delete_all_from_parent_graph(parent_id)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}




@crud_router.post("/CRUD/update/process_meta_data/", tags=["Specific Process Update Operations"])
async def update_process_data_meta_data(updated_instance:Process_update_meta_data_schema):
    """
    Endpoint to update process meta data.

    **Parameters:**
    - **updated_instance**: An instance of Process_update_meta_data_schema containing the updated meta data.

    **Returns:**
    - A result indicating the success of the update, otherwise raises a 404 HTTP exception.
    """
    updated_meta_data = updated_instance.dict()
    result = update_process_meta_data(**updated_meta_data)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}

@crud_router.post("/CRUD/update/process_elastic_data_paths/", tags=["Specific Process Update Operations"])
async def update_process_data_elastic_data_paths(updated_instance:Process_update_elastic_data_paths_schema):
    """
    Endpoint to update process elastic data paths.

    **Parameters:**
    - **updated_instance**: An instance of Process_update_elastic_data_paths_schema containing the updated elastic data paths.

    **Returns:**
    - A result indicating the success of the update, otherwise raises a 404 HTTP exception.
    """
    updated_elastic_data_paths = updated_instance.dict()
    result = update_process_elastic_data_paths(**updated_elastic_data_paths)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}

@crud_router.post("/CRUD/update/graph_process_meta_data/", tags=["Specific Graph Update Operations"])
async def update_graph_data_process_meta_data(updated_instance:Graph_update_meta_data_schema):
    """
    Endpoint to update graph process meta data.

    **Parameters:**
    - **updated_instance**: An instance of Graph_update_meta_data_schema containing the updated meta data.

    **Returns:**
    - A result indicating the success of the update, otherwise raises a 404 HTTP exception.
    """
    updated_process_meta_data = updated_instance.dict()
    result = update_graph_process_meta_data(**updated_process_meta_data)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}

@crud_router.post("/CRUD/update/graph_project_name/", tags=["Specific Graph Update Operations"])
async def update_graph_data_project_name(updated_instance:Graph_update_project_name_schema):
    """
    Endpoint to update graph project name.

    **Parameters:**
    - **updated_instance**: An instance of Graph_update_project_name_schema containing the updated project name.

    **Returns:**
    - A result indicating the success of the update, otherwise raises a 404 HTTP exception.
    """
    updated_project_name = updated_instance.dict()
    result = update_graph_project_name(**updated_project_name)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}

@crud_router.post("/CRUD/update/graph_owner_email/", tags=["Specific Graph Update Operations"])
async def update_graph_data_owner_email(updated_instance:Graph_update_owner_email_schema):
    """
    Endpoint to update graph owner email.

    **Parameters:**
    - **updated_instance**: An instance of Graph_update_owner_email_schema containing the updated owner email.

    **Returns:**
    - A result indicating the success of the update, otherwise raises a 404 HTTP exception.
    """
    updated_owner_email = updated_instance.dict()
    result = update_graph_owner_email(**updated_owner_email)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}

@crud_router.post("/CRUD/update/graph_owner/", tags=["Specific Graph Update Operations"])
async def update_graph_data_owner(updated_instance:Graph_update_owner_schema):
    """
    Endpoint to update graph owner.

    **Parameters:**
    - **updated_instance**: An instance of Graph_update_owner_schema containing the updated owner information.

    **Returns:**
    - A result indicating the success of the update, otherwise raises a 404 HTTP exception.
    """
    updated_owner = updated_instance.dict()
    result = update_graph_owner(**updated_owner)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}

@crud_router.post("/CRUD/update/process_list_order/", tags=["Specific Graph Update Operations"])
async def update_graph_data_process_list_order(updated_instance:Graph_update_process_list_order):
    """
    Endpoint to update graph process list order.
    Please note that supplied values should contain all of the instances
    currently in the process list, just in a different order

    **Parameters:**
    - **updated_instance**: An instance of Graph_update_owner_schema containing the updated list order.

    **Returns:**
    - A result indicating the success of the update, otherwise raises a 404 HTTP exception.
    """
    updated_process_list = updated_instance.dict()
    result = update_graph_process_list_order(**updated_process_list)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}

@crud_router.post("/CRUD/create/graph/", tags=["Graph Create Operations"])
async def create_graph(new_graph:GraphMap):
    """
    Endpoint to create a new graph document.

    **Parameters:**
    - **new_graph**: An instance of GraphMap containing the graph document data.

    **Returns:**
    - A result indicating the success of the graph creation, otherwise raises a 404 HTTP exception.
    """
    new_graph_dict = new_graph.dict()

    # Generate internal _id
    new_graph_dict["_id"] = str(uuid.uuid4())
    result = create_graph_document(new_graph_dict)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}

@crud_router.post("/CRUD/create/process/", tags=["Process Create Operations"])
async def create_process(new_process:ProcessStep, list_insert_location:int = None):
    """
    Endpoint to create a new process.

    **Parameters:**
    - **new_process**: An instance of ProcessStep containing the process data.
    - **list_insert_location**: Optional parameter indicating the location to 
                                insert the new process in the parent list.

    **Returns:**
    - A result indicating the success of the process creation, otherwise raises a 404 HTTP exception.
    """
    new_process_dict = new_process.dict()

    # Generate internal _id
    new_process_dict["_id"] = str(uuid.uuid4())
    result = create_process_document(new_process_dict, list_insert_location=list_insert_location)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}


