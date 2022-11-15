from pymongo import MongoClient
from pymongo.collection import Collection
from scrapers.interface import JobSummary, JobDetails
from typing import List
from .models import MongoJob

class DBMongoClient:
    PORT = 27018
    DOCUMENT_NAME = 'FindJobs'

    def __init__(self) -> None:
        client = MongoClient("mongodb://localhost:27018/")
        self._db = client["FindJobs"]

    @property
    def offers(self) -> Collection:
        return self._db["Offers"]

    def insert_jobs(self, jobs: List[JobDetails]):
        items = [MongoJob(**item.__dict__) for item in jobs]

        return self.offers.insert_many([item.__dict__ for item in items])

    def filter_unknowing_jobs(self, jobs: List[JobSummary], portal: str) -> List[JobSummary]:
        pipeline = [
            {
                '$match': {
                    "$expr": {
                        "$and": {
                            "$or": [
                                {"$in": ['$id', [job.id for job in jobs]]},
                                {"$in": ['$url', [job.url for job in jobs]]},
                            ],
                            "$eq": ['$portal', portal]
                        }
                    }
                }
            }
        ]

        result = self.offers.aggregate(pipeline)


