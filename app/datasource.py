import pandas as pd
import os

from app.schemas import Item


def initialize_items():
    items = []
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'inventory.csv')
    data = pd.read_csv(file_path)
    for index, row in data.iterrows():
        items.append(Item(**row))
    return items
