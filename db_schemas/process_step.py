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

class ProcessStep(BaseModel):
    """
    Pydantic model for structuring process step data.

    Attributes:
        id (str): The unique identifier for the process step document.
        parent_graph (str): The ID of the parent graph document.
        meta_data (Dict[str, Any]): Metadata for the process step.
        elastic_data_paths (Dict[str, Any]): Paths to the elastic data.
        date_created (datetime): The creation timestamp.
        date_updated (datetime): The last updated timestamp.
    """
    parent_graph: str
    meta_data: Dict[str, Any] = Field(default_factory=dict)
    elastic_data_paths: Dict[str, Any] = Field(default_factory=dict)
    file_location_type: Literal[
                            'digs_local', 
                            'pool', 
                            'embedded', 
                            'mixed'
                        ]
    date_created: datetime = Field(default_factory=datetime.utcnow)
    date_updated: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        """
        Pydantic configuration for the model.
        """
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.strftime('%Y-%m-%dT%H:%M:%S')
        }
