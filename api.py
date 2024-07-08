"""
-------------------------------------------------------------------
This is a Goldfish Project File

Authors: Max Witwer, Jie Chen, Elliott Cole
Collaboration with the Baker Lab

This file was generated during an internship at the institute for
protein design

Description:
This is the main api file that links all routes together
and sets up the swagger config

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
    },
    {
        "name": "Specific Process Delete Operations",
        "description": "Endpoints that delete specfic process documents",
    },
    {
        "name": "Specific Graph Delete Operations",
        "description": "Endpoints that delete specfic graph documents",
    },
    {
        "name": "Specific Process Update Operations",
        "description": "Endpoints that update specfic process documents",
    },
    {
        "name": "Specific Graph Update Operations",
        "description": "Endpoints that update specfic graph documents",
    },
    {
        "name": "Graph Create Operations",
        "description": "Endpoints relating to creation of graph documents",
    },
    {
        "name": "Process Create Operations",
        "description": "Endpoints relating to creation of process documents",
    }
]
docs_text = open('display_text.txt', 'r').read()

# generate app instance
app = FastAPI(
    title="Goldfish Documentation",
    description=docs_text,
    version="1.0.0",
    openapi_tags=tags_metadata
)

# include the router
app.include_router(crud_router)

