import os
from typing import List

import strawberry
from strawberry.asgi import GraphQL
import pandas as pd
from fastapi import FastAPI

from app.swagger import custom_openapi
from app.schemas import Item


app = FastAPI()

@strawberry.type
class Query:
    @strawberry.field
    def items(self, info) -> List[Item]:
        return items
schema = strawberry.Schema(query=Query)
app.add_route("/graphql", GraphQL(schema=schema))

# Custom OpenAPI schema for swagger in /docs
app.openapi = lambda: custom_openapi(app)

items = []
def initialize_items(file_path):
    data = pd.read_csv(file_path)
    for index, row in data.iterrows():
        items.append(Item(**row))

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'inventory.csv')
initialize_items(file_path)
