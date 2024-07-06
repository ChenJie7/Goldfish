from pydantic import BaseModel, Field, EmailStr, root_validator
from typing import List, Dict, Any
from bson import ObjectId
from datetime import datetime

class ProcessStep(BaseModel):
    id: ObjectId = Field(ObjectId, alias="_id")
    parent_graph: ObjectId
    meta_data: Dict[str, Any]
    elastic_data_paths: Dict[str, Any]
    date_created: datetime
    date_updated: datetime

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.strftime('%Y-%m-%dT%H:%M:%S')
        }

    @root_validator(pre=True)
    def include_id(cls, values):
        if 'id' in values:
            values['_id'] = values.pop('id')
        return values

    def dict(self, *args, **kwargs):
        result = super().dict(*args, **kwargs)
        if 'id' in result:
            result['_id'] = result.pop('id')
        return result
