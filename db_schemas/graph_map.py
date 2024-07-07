"""
-------------------------------------------------------------------
This is a Goldfish Project File

Authors: Max Witwer, Jie Chen, Elliot Cole
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
    id: str = Field(str, alias="_id")
    project_name: str
    process_list: List[str]
    process_meta_data: Dict[str, Any]
    owner: str
    owner_email: EmailStr
    date_created: datetime
    date_updated: datetime

    class Config:
        """
        Pydantic configuration for the model.
        """
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.strftime('%Y-%m-%dT%H:%M:%S')
        }

    @root_validator(pre=True)
    def include_id(cls, values):
        """
        Root validator to handle the inclusion of the `id` field.
        
        Ensures that if `id` is present in the values, it is mapped to `_id`.

        :param values: The values being validated.
        :return: The updated values with `_id` included if `id` was present.
        """
        if 'id' in values:
            values['_id'] = values.pop('id')
        return values

    def dict(self, *args, **kwargs):
        """
        Override the `dict` method to ensure `_id` is included in the output.

        :return: The dictionary representation of the model.
        """
        result = super().dict(*args, **kwargs)
        if 'id' in result:
            result['_id'] = result.pop('id')
        return result
