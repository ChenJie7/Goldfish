# routes.py
from fastapi import APIRouter, HTTPException
from CRUD_utils import *
import json

crud_router = APIRouter()

@crud_router.get("/CRUD/read/graph_instance/{filter}", tags=["General Graph Read Operations"])
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

@crud_router.get("/CRUD/read/graph_collection/{filter}", tags=["General Graph Read Operations"])
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

@crud_router.get("/CRUD/read/process_instance/{filter}", tags=["General Process Read Operations"])
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

@crud_router.get("/CRUD/read/process_collection/{filter}", tags=["General Process Read Operations"])
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

