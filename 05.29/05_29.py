# Task Nr.3:
# With your own tool, create of database of grocery store. Store consist three different categories of items (lets say electronics, fruits, food etc.).
#  The items as minimum should have these fields: name, price, quantity, year made (YYYY-MM-DD). Task:

# Get all electronic items monetary value made 1 years, 2 months and 12 days from today.
# Get average price for all items/categories in the store.
# Get all items which names starts with letter a, and cost is between 10 and 100.
# Find all item names (only) for prices > 50 and quantity < 10.

from typing import Any, List
from pymongo import MongoClient
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import *

# pylint: disable-all


def get_utc_timestamp(year: int, month: int, day: int) -> float:
    now = datetime.now()
    past_date = now - relativedelta(years=year, months=month, days=day)
    past_timestamp = past_date.replace(tzinfo=timezone.utc).timestamp()
    return past_timestamp


class Base:
    def __init__(self) -> Any:
        self.client = MongoClient("mongodb://localhost:27017/")


    def get_db(self):
        return self.db

    @staticmethod
    def sum_price_from_documents(documents) -> float:
        price_list = [document["price"] for document in documents]
        sum_pice = round(sum(map(float, price_list)), 2)
        return sum_pice

    @staticmethod
    def average_price_from_documents(list_price: list) -> float:
        return round(sum(list_price) / len(list_price), 2)

    def get_collection_names(self) -> list[str]:
        return self.db.list_collection_names()


class Collections(Base):
    def __init__(self, db: str, collection: str = None) -> Any:
        super().__init__()
        self.db = self.get_db(db)
        self.collection_name = collection
        self.collection = self.db[self.collection_name]

    def filter_documents(self, date_ts, field_names):
        query = {field_names: {"$gt": date_ts}}
        result = self.collection.find(query)
        return result

    def get_all_from_collection(self):
        result = self.collection.find()
        return result

    def get_documents_where_start_and_cost_between_cost(
        self, start: str, cost1: str, cost2: str, field_name: str
    ) -> List[dict]:
        query = {
            field_name: {"$regex": f"(\s+{start}|^{start})", "$options": "i"},
            "price": {"$gt": cost1, "$lt": cost2},
        }
        result = self.collection.find(query)

        return list(result)

    def get_documents_where_price_more_value1_and_price_less_value2(
        self, field_name: str, value1: int, value2: int
    ) -> List[dict]:
        query = {"$or": [{field_name: {"$gt": value1}}, {field_name: {"$lt": value2}}]}
        result = self.collection.find(query, {"name": 1, "price": 1})
        return list(result)


db = Collections(collection="electronics", db="store")
documents = db.filter_documents(
    date_ts=get_utc_timestamp(1, 2, 12),
    field_names="date_ts",
)
print(Base.sum_price_from_documents(documents=documents))


collections = db.get_collection_names()
price_list = []
for x in collections:
    db.collection_name = x
    result = db.get_all_from_collection()
    for price in result:
        price_list.append(price["price"])

print(Base.average_price_from_documents(list_price=price_list))

collections = db.get_collection_names()
for x in collections:
    db.collection_name = x
    result = db.get_documents_where_start_and_cost_between_cost(
        start="c", field_name="name", cost1=10, cost2=100
    )
    print(result)
print(
    "________________________________________________________________________________________________________________________________________________________________________________________________"
)

for x in collections:
    db.collection_name = x
    result = db.get_documents_where_price_more_value1_and_price_less_value2(
        field_name="price", value1=50, value2=10
    )
    print(result)

print(
    "________________________________________________________________________________________________________________________________________________________________________________________________"
)
