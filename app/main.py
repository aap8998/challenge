from typing import List

import strawberry
from strawberry.asgi import GraphQL
from fastapi import FastAPI, Query

from app.openapi import custom_openapi
from app.schemas import Item
from app.datasource import initialize_items
from app.nlp import text_search

app = FastAPI()


# GraphQL endpoint
@strawberry.type
class Query:
    @strawberry.field
    def items(self, info) -> List[Item]:
        return items


schema = strawberry.Schema(query=Query)
app.add_route("/graphql", GraphQL(schema=schema))


# OpenAPI schema for /docs
app.openapi = lambda: custom_openapi(app)


# Natural language processing endpoint
@app.get("/nlp")
async def search_nlp(q: str, lang: str = "en"):
    result = await text_search(q, lang)
    return {"result": result}


# Initialize the items list
items = initialize_items()
