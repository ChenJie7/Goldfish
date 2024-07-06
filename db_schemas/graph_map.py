from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Any
from bson import ObjectId
from datetime import datetime

class GraphMap(BaseModel):
    _id: ObjectId
    project_name: str
    process_list: List[ObjectId]
    process_meta_data: Dict[str, Any]
    owner: str
    owner_email: EmailStr
    date_created: datetime
    date_updated: datetime

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.strftime('%Y-%m-%dT%H:%M:%S')
        }
