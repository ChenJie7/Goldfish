from pydantic import BaseModel, Field, EmailStr
from typing import List, Dict, Any
from bson import ObjectId
from datetime import datetime


# Example usage
graph_map_ID = ObjectId()
process_step_IDs = [ObjectId() for _ in range(10)]
time_stamp = datetime.now()

example_graph_inst = {
    "_id": graph_map_ID,
    "project_name": "Example Schema",
    "process_list": process_step_IDs,
    "process_meta_data": {"description": "variable meta data goes here"},
    "owner": "Max Witwer",
    "owner_email": "mwitwer@uw.edu",
    "date_created": time_stamp,
    "date_updated": time_stamp
}

example_process_inst = [{
    "_id": process_step_IDs[i],
    "parent_graph": graph_map_ID,
    "meta_data": {"description": "variable meta data goes here"},
    "elastic_data_paths": {
        "pdb": ["/some_path1.pdb", "/some_path2.pdb", "/some_path3.pdb"]
    },
    "date_created": time_stamp,
    "date_updated": time_stamp
} for i in range(len(process_step_IDs))]

graph_map = GraphMap(**example_graph_inst)
process_steps = [ProcessStep(**process) for process in example_process_inst]

print(graph_map.json())
print([process.json() for process in process_steps])
