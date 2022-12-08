from typing import Protocol
from fastapi import FastAPI
from db import DBMongoClient

class ResourceCollection:

    def __init__(self, app: FastAPI, db: DBMongoClient) -> None:
        self.app = app
        self.db = db


