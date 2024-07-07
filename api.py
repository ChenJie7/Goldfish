"""
-------------------------------------------------------------------
This is a Goldfish Project File

Authors: Max Witwer, Jie Chen, Elliot Cole
Collaboration with the Baker Lab

This file was generated during an internship at the institute for
protein design

Description:
This file contains all FastAPI endpoints that allow for querying 
the database. It provides read operations for graph and process 
collections within the MongoDB database, enabling CRUD functionality 
via HTTP requests. The endpoints are categorized for better 
documentation and ease of use.

Date: 07/06/2024
-------------------------------------------------------------------
"""

from fastapi import FastAPI, HTTPException
from CRUD_utils import *
import json

from routes.crud import crud_router

# meta data for autodocumentation
tags_metadata = [
    {
        "name": "General Graph Read Operations",
        "description": "Endpoints that relate to reading arbitrary graph collection documents",
    },
    {
        "name": "Specific Graph Read Operations",
        "description": "Endpoints that relate to reading from specific graph fields",
    },
    {
        "name": "General Process Read Operations",
        "description": "Endpoints that relate to reading arbitrary process collection documents",
    },
    {
        "name": "Specific Process Read Operations",
        "description": "Endpoints that relate to reading from specific process fields",
    }
]

docs_text = open('display_text.txt', 'r').read()

# generate app instance
app = FastAPI(
    title="Goldfish Doumentation",
    description=docs_text,
    version="1.0.0",
    openapi_tags=tags_metadata
)

# include the router
app.include_router(crud_router)

