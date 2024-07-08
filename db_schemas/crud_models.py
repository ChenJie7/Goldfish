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

# Define the data model
class Process_update_meta_data_schema(BaseModel):
    update_id: str
    meta_data: Dict[str, Any]
    
# Define the data model
class Process_update_elastic_data_paths_schema(BaseModel):
    update_id: str
    elastic_data_paths: Dict[str, Any]

# Define the data model
class Process_update_file_location_type_schema(BaseModel):
    update_id: str
    file_location_type: Literal[
                            'digs_local', 
                            'pool', 
                            'embedded', 
                            'mixed'
                        ]