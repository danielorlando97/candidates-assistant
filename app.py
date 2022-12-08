from pydantic import BaseModel
from db import DBMongoClient, JobDetails
from fastapi import FastAPI, Query, Depends
from typing import List, Union
from services import search, security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from inner_core.resources import ResourceCollection
import requests
from fastapi.responses import HTMLResponse

app = FastAPI()
# db = DBMongoClient()
# resource = ResourceCollection(app, db)

############################################################

#               Loading Route

###########################################################

# search.load_routes(resource)
# security.load_routes(resource)



@app.get("/", response_class=HTMLResponse)
async def read_items():
    html_content = requests.get('http://localhost:8010').content.decode()
    return HTMLResponse(content=html_content, status_code=200)