from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Any
from bson import ObjectId
from datetime import datetime

class ProcessStep(BaseModel):
    _id: ObjectId 
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
