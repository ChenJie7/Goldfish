# routes.py
from fastapi import APIRouter, HTTPException
from CRUD_utils import *
import json

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

@crud_router.post("/CRUD/update/process_file_location_type/", tags=["Specific Process Update Operations"])
async def update_process_data_file_location_type(updated_instance:Process_update_file_location_type_schema):
    """
    Endpoint to update process file location type.

    **Parameters:**
    - **updated_instance**: An instance of Process_update_file_location_type_schema containing the updated file location type.

    **Returns:**
    - A result indicating the success of the update, otherwise raises a 404 HTTP exception.
    """
    updated_file_location_type = updated_instance.dict()
    result = update_process_file_location_type(**updated_file_location_type)
    if not result:
        raise HTTPException(status_code=404, detail="Processes not found")
    return {"result": result}


