# Task Nr.3:
# With your own tool, create of database of grocery store. Store consist three different categories of items (lets say electronics, fruits, food etc.).
#  The items as minimum should have these fields: name, price, quantity, year made (YYYY-MM-DD). Task:

# Get all electronic items monetary value made 1 years, 2 months and 12 days from today.
# Get average price for all items/categories in the store.
# Get all items which names starts with letter a, and cost is between 10 and 100.
# Find all item names (only) for prices > 50 and quantity < 10.

from typing import Any, List, Optional, Union
from pymongo import MongoClient
from datetime import datetime, timedelta, timezone
from dateutil.relativedelta import *
from pymongo.errors import (
    ConnectionFailure,
    PyMongoError,
    ServerSelectionTimeoutError,
    CollectionInvalid,
    ExecutionTimeout,
    OperationFailure,
)
import time

# pylint: disable-all


def get_utc_timestamp(year: int, month: int, day: int) -> float:
    now = datetime.now()
    past_date = now - relativedelta(years=year, months=month, days=day)
    past_timestamp = past_date.replace(tzinfo=timezone.utc).timestamp()
    return past_timestamp


class Base:
    def __init__(self) -> Any:
        self.client = MongoClient(
            "mongodb://localhost:27016/", serverSelectionTimeoutMS=5000
        )

    def get_db(self, db: str) -> Optional[MongoClient]:
        try:
            self.db = self.client[db]
            self.client.server_info()
            return self.db

        except ServerSelectionTimeoutError as e:
            print("Connection failure:", str(e))
            raise Exception("Connection failure")

        except PyMongoError as e:
            print("An error occurred:", str(e))
            exit()

    @staticmethod
    def sum_price_from_documents(documents) -> float:
        price_list = [document["price"] for document in documents]
        sum_price = round(sum(map(float, price_list)), 2)
        return sum_price

    @staticmethod
    def average_price_from_documents(list_price: list) -> float:
        return round(sum(list_price) / len(list_price), 2)

    def get_collection_names(self) -> list[str]:
        try:
            return self.db.list_collection_names()
        except PyMongoError as e:
            print("An error occurred:", str(e))
            exit()

    def execute_with_retry(self, func, db):
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                live_db = func(db)
                return live_db
            except Exception as e:
                print(f"Execution failed: {e}")
                retries += 1
                print(f"Retrying... (Attempt {retries}/{max_retries})")
                time.sleep(1)
        else:
            print("Maximum retries exceeded. Giving up.")
            exit()


class Collections(Base):
    def __init__(self, db: str, collection: str = None) -> Any:
        super().__init__()
        self.db = self.execute_with_retry(self.get_db, db)
        self.collection_name = collection
        self.collection = self.db[self.collection_name]

    def filter_documents(self, date_ts, field_names) -> Union[List[dict], str]:
        try:
            query = {field_names: {"$gt": date_ts}}
            result = self.collection.find(query)
            return result

        except ExecutionTimeout as e:
            return f"Query execution timeout:, {str(e)}"

        except PyMongoError as e:
            return f"An error occurred:, {str(e)}"

    def get_all_from_collection(self):
        try:
            result = self.collection.find()
            return result

        except ExecutionTimeout as e:
            return "Query execution timeout:", str(e)

        except PyMongoError as e:
            return "An error occurred:", str(e)

    def get_documents_where_start_and_cost_between_cost(
        self, start: str, cost1: str, cost2: str, field_name: str
    ) -> Union[List[dict], str]:
        try:
            query = {
                field_name: {"$regex": f"(\s+{start}|^{start})", "$options": "i"},
                "price": {"$gt": cost1, "$lt": cost2},
            }
            result = self.collection.find(query)
            return list(result)

        except ExecutionTimeout as e:
            return f"Query execution timeout:, {str(e)}"

        except PyMongoError as e:
            return f"An error occurred:, {str(e)}"

    def get_documents_where_price_more_value1_and_price_less_value2(
        self, field_name: str, value1: int, value2: int
    ) -> Union[List[dict], str]:
        try:
            query = {
                "$or": [{field_name: {"$gt": value1}}, {field_name: {"$lt": value2}}]
            }
            result = self.collection.find(query, {"name": 1, "price": 1})
            return list(result)

        except ExecutionTimeout as e:
            return f"Query execution timeout:, {str(e)}"

        except PyMongoError as e:
            return f"An error occurred:, {str(e)}"


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
