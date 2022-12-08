from inner_core.resources import ResourceCollection
from typing import List
from fastapi import Query, Depends

class SearchQuery:  
    def __init__(self, 
        kwds: List[str] = Query(default=[]), 
        limit: int  = Query(default=10, gt = 1), 
        skip: int = Query(default=0, ge = 0)
    ) -> None:
        
        self.kwds: List[str] = kwds 
        self.limit: int = limit
        self.skip: int = skip


def load_routes(rc: ResourceCollection):
    app = rc.app
    db = rc.db
    
    @app.get('/boolean_search/')
    async def _(q: SearchQuery = Depends()):
        def clean_result(x):
            del x['_id']
            x['Doc']['_id'] = str(x['Doc']['_id'])
            return x

        result = db.ranking(q.kwds, q.limit, q.skip)
        result = list(map(clean_result, result))
        return {
            'data': result,
            'meta': {
                "query": q
            }
        }
