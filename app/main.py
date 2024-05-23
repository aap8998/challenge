from fastapi import FastAPI
from strawberry.asgi import GraphQL
import strawberry
from typing import List
import pandas as pd
import os


@strawberry.type
class Item:
    id: str
    name: str

@strawberry.type
class Query:
    @strawberry.field
    def items(self, info) -> List[Item]:
        return items

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'inventory.csv')
schema = strawberry.Schema(query=Query)

items = []

def initialize_items(file_path):
    data = pd.read_csv(file_path)
    for index, row in data.iterrows():
        items.append(Item(id=row['desc_ga_sku_producto'], name=row['desc_ga_nombre_producto_1']))

initialize_items(file_path)

app = FastAPI()
app.add_route("/graphql", GraphQL(schema=schema, ))
