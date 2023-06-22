# Task Nr.1 : Create the CLI application, that would populate MongoDB database with random data. The input should ask for :

# database name
# collection name
# field name with types (string, number, date string objects etc.) with range of values (lets say field name = price , then value is number (float, int) which is random number from a(min) to b(max) )
# number o documents to create.
# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long , import-error



from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List, Any
import string
import random
from tqdm import tqdm
from datetime import datetime, timedelta, timezone
from py_random_words import RandomWords


class MongoDB:
    def __init__(self, host: str, port: int, db_name: str, collection_name):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]


    def create_document(self, task: Dict[str, Any]) -> str:
        result = self.collection.insert_one(task)
        return str(result.inserted_id)

def get_db_name()-> str:
    return input("Enter database name: ")

def get_collection_name()-> str:
    return input("Enter collection name: ")

def get_field_name() -> str:
    return input("Enter field name: ")

def get_number_of_fields() -> int:
    return int(input("Enter number of fields (string, integer, float , date): "))

def get_field_type() -> str:
    return input("Enter field type: ")

def get_min_value() -> int:
    return int(input("Enter minimal value: "))

def get_max_value() -> int:
    return int(input("Enter maximal value: "))

def how_many_documents():
    return int(input("How many documents?: "))

def add_fealds_q():
    return input("Maybe you want to add a field?: (Y/N)")

def get_string_field_value():
     r = RandomWords()
     r.get_word()
     return r.get_word()

def get_integer_field_value(min_value, max_value):
    return random.randint(min_value, max_value)

def get_float_field_value(min_value: float, max_value: float) -> float:
    return random.uniform(min_value, max_value)

def or_repeat():
    repeat = input('repeat: Y/N? ')
    if repeat == 'Y':
        return True
    else:
        return False
    
def get_random_date_ts():
    datetime_now = datetime.now()
    datetime_after = datetime_now - timedelta(days=1095)
    ts_now = datetime_now.replace(tzinfo=timezone.utc).timestamp()
    ts_after = datetime_after.replace(tzinfo=timezone.utc).timestamp()
    random_date = random.uniform(ts_now,ts_after)
    return random_date
    

def generator(field_name, field_type, min_value = None, max_value = None):
    document = {}
    while True:
        if field_type == "string":
            document["date_ts"] = get_random_date_ts()
            document[field_name] = get_string_field_value()
        elif field_type == "integer":
            document["date_ts"] = get_random_date_ts()
            document[field_name] = get_integer_field_value(min_value= min_value, max_value= max_value)
        elif field_type == "float":
            document["date_ts"] = get_random_date_ts()
            document[field_name] = get_float_field_value(min_value= min_value, max_value= max_value)
        elif field_type == "date":
            document["date_ts"] = get_random_date_ts()


        return document

def get_str(field_name):
    doc = {"date_ts": get_random_date_ts(),
         field_name: get_string_field_value()}
    return doc

def helper():
    min_value = None
    max_value = None
    field_name = get_field_name()
    field_type = get_field_type()

    if field_type == "integer":
        min_value = get_min_value()
        max_value = get_max_value()
    elif field_type == "float":
        min_value = get_min_value()
        max_value = get_max_value()
    return field_name, field_type, min_value, max_value



if __name__ == "__main__":
    host = "localhost"
    port = 27017
    db_name = get_db_name()
    collection_name = get_collection_name()
    db = MongoDB(host= host, port= port, db_name= db_name, collection_name= collection_name)
    repeat = True

    while True:
        doc_much = how_many_documents()
        document = {}
        while repeat:

            field_name, field_type, min_value, max_value = helper()

            doc_str = get_str(field_name)
            document.update(doc_str)
 
            choice = add_fealds_q()
            if choice == "Y":
                continue

            # db.create_document(document)
 
            repeat = or_repeat()

        exit()