"""
-------------------------------------------------------------------
This is a Goldfish Project File

Authors: Max Witwer, Jie Chen, Elliott Cole
Collaboration with the Baker Lab

This file was generated during an internship at the institute for
protein design

Description:
Schema for loading and structuring graph data field


Date: 07/06/2024
-------------------------------------------------------------------
"""

from pydantic import BaseModel, Field, EmailStr, root_validator
from typing import List, Dict, Any
from datetime import datetime

import uuid

class GraphMap(BaseModel):
    """
    Pydantic model for structuring graph data.

    Attributes:
        id (str): The unique identifier for the graph document.
        project_name (str): The name of the project.
        process_list (List[str]): A list of process IDs associated with the graph.
        process_meta_data (Dict[str, Any]): Metadata for processes.
        owner (str): The owner of the project.
        owner_email (EmailStr): The email of the project owner.
        date_created (datetime): The creation timestamp.
        date_updated (datetime): The last updated timestamp.
    """
    project_name: str
    process_list: List[str] = Field(default_factory=list)
    process_meta_data: Dict[str, Any] = Field(default_factory=dict)
    owner: str
    owner_email: EmailStr
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
