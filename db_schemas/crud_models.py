"""
-------------------------------------------------------------------
This is a Goldfish Project File

Authors: Max Witwer, Jie Chen, Elliott Cole
Collaboration with the Baker Lab

This file was generated during an internship at the institute for
protein design

Description:
Schema for loading and structuring process step data

Date: 07/06/2024
-------------------------------------------------------------------
"""

from pydantic import BaseModel, Field, EmailStr, root_validator
from typing import List, Dict, Any, Literal
from datetime import datetime

class Process_update_meta_data_schema(BaseModel):
    """
    Pydantic model for process update metadata.

    Attributes:
        update_id (str): The unique identifier for the update.
        meta_data (Dict[str, Any]): Metadata associated with the update.
    """
    update_id: str
    meta_data: Dict[str, Any]
    
class Process_update_elastic_data_paths_schema(BaseModel):
    """
    Pydantic model for process update elastic data paths.

    Attributes:
        update_id (str): The unique identifier for the update.
        elastic_data_paths (Dict[str, Any]): Elastic data paths associated with the update.
    """
    update_id: str
    elastic_data_paths: Dict[str, Any]

class Process_update_file_location_type_schema(BaseModel):
    """
    Pydantic model for process update file location type.

    Attributes:
        update_id (str): The unique identifier for the update.
        file_location_type (Literal): The type of file location, restricted to specific values.
    """
    update_id: str
    file_location_type: Literal[
                            'digs_local', 
                            'pool', 
                            'embedded', 
                            'mixed'
                        ]


class Graph_update_project_name_schema(BaseModel):
    """
    Pydantic model for graph update project name.

    Attributes:
        update_id (str): The unique identifier for the update.
        project_name (str): The name of the project.
    """
    update_id: str
    project_name: str

class Graph_update_owner_email_schema(BaseModel):
    """
    Pydantic model for graph update owner email.

    Attributes:
        update_id (str): The unique identifier for the update.
        owner_email (str): The email of the project owner.
    """
    update_id: str
    owner_email: str

class Graph_update_owner_schema(BaseModel):
    """
    Pydantic model for graph update owner.

    Attributes:
        update_id (str): The unique identifier for the update.
        owner (str): The owner of the project.
    """
    update_id: str
    owner: str

class Graph_update_meta_data_schema(BaseModel):
    """
    Pydantic model for graph update metadata.

    Attributes:
        update_id (str): The unique identifier for the update.
        process_meta_data (Dict[str, Any]): Metadata associated with the process.
    """
    update_id: str
    process_meta_data: Dict[str, Any]

class Graph_update_process_list_order(BaseModel):
    """
    Pydantic model for updating the order of the process lists.

    Attributes:
        update_id (str): updated process list in the new order containing 
        all values from the original list.
        process_meta_data (Dict[str, Any]): Metadata associated with the process.
    """
    update_id: str
    process_list: List[str]



