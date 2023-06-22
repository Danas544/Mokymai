# Task Nr.1 :
# Create a simple database (type of db, collections, fields - pick your own) with your db creation tool and incorporate
# all new querying operators with the results.

from typing import Any, List
from pymongo import MongoClient

# pylint: disable-all


class Base:
    def __init__(self, db: str, collection: str) -> Any:
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db]
        self.collection_name = collection
        self.collection = self.db[self.collection_name]

    def filter_gte(self, field_name: str, value: str) -> List[dict]:
        query = {field_name: {"$gte": value}}
        result = self.collection.find(query)
        return list(result)

    def filter_lte(self, field_name: str, value: str) -> List[dict]:
        query = {field_name: {"$lte": value}}
        result = self.collection.find(query)
        return list(result)

    def filter_in(self, field_name: str, value: List[str]) -> List[dict]:
        query = {field_name: {"$in": value}}
        result = self.collection.find(query)
        return list(result)

    def filter_nin(self, field_name: str, value: List[str]) -> List[dict]:
        query = {field_name: {"$nin": value}}
        result = self.collection.find(query)
        return list(result)


db = Base("0531DB", collection="Cats")
print("filter_gte________________________________________________________________")
print(db.filter_gte(field_name="quantity", value=95))

db.collection_name = "Dogs"
print("filter_lte________________________________________________________________")
print(db.filter_lte(field_name="quantity", value=10))

db.collection_name = "Cats"
print("filter_by_in________________________________________________________________")
my_list = ["parakeet", "vicuna", "toucan"]
print(db.filter_in(field_name="name", value=my_list))

print("filter_by_nin________________________________________________________________")
print(db.filter_nin(field_name="name", value=my_list))
