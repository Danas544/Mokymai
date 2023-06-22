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
    return int(input("Maybe you want to add a field?: (Y/N)"))

def get_string_field_value():
     r = RandomWords()
     r.get_word()
     return r.get_word()

def get_integer_field_value(min_value = 1, max_value = 100):
    return random.randint(min_value, max_value)

def get_float_field_value(min_value: float = 1.00, max_value: float = 100.00) -> float:
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
    





if __name__ == "__main__":
    host = "localhost"
    port = 27017
    db_name = get_db_name()
    collection_name = get_collection_name()
    db = MongoDB(host= host, port= port, db_name= db_name, collection_name= collection_name)
    repeat = True
    doc = how_many_documents()
    while repeat:
        field_name = get_field_name()
        field_type = get_field_type()

        if field_type == "integer":
            min_value = get_min_value()
            max_value = get_max_value()
        elif field_type == "float":
            min_value = get_min_value()
            max_value = get_max_value()


            # print(document)
        
# Reujua persidaryti , kad klausti ar add feald 
        for i in tqdm (range (doc), desc="Loading…", ascii=False, ncols=75):
            document = {}
            if field_type == "string":
                document[field_name] = get_string_field_value()
                document["price"] =  round(get_float_field_value(),3)
                document["quantity"] = get_integer_field_value()
                document["date_ts"] = get_random_date_ts()
            elif field_type == "integer":
                document[field_name] = get_integer_field_value(min_value= min_value, max_value= max_value)
                document["date_ts"] = get_random_date_ts()
            elif field_type == "float":
                document[field_name] = get_float_field_value(min_value= min_value, max_value= max_value)
                document["date_ts"] = get_random_date_ts()
            elif field_type == "date":
                document[field_name] = get_float_field_value(min_value= min_value, max_value= max_value)
                document["date_ts"] = get_random_date_ts()


            db.create_document(document)
            
        repeat = or_repeat()
        if repeat is True:
            continue

    exit()