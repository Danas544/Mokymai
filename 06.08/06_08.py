# Task Nr.1 : Using all Exceptions explained above, create a simple application(s) to test (if possible in local environment) all of them.
# Use Docker Container for live connection.


from pymongo import MongoClient
from typing import List, Any
from pymongo.errors import ConnectionFailure, PyMongoError, ServerSelectionTimeoutError , CollectionInvalid , ExecutionTimeout, OperationFailure


class Base:
    def __init__(self) -> Any:
        self.adress = None
        self.port = None
        self.database_name = None
        self.collection_name = None

    def connect_to_db(self) -> MongoClient:
        connection = f"{self.adress}:{self.port}"
        try:
            client = MongoClient(f"mongodb://{connection}",serverSelectionTimeoutMS=5000)
            client.server_info()
            return client

        except ServerSelectionTimeoutError as e:
            print("Connection failure:", str(e))
            return client

        except PyMongoError as e:
            print("An error occurred:", str(e))
            return None
        
    def query_databases(self, client: MongoClient , value: str):
        try:
            db = client[self.database_name]
            collection = db[self.collection_name]

            result = collection.find_one({'name': value})

            if result:
                return f'Found document: {result}'
            else:
                return 'Document not found.'

        except PyMongoError as e:
            return e, False

    def create_collection(self, collection_name: str)-> bool:
        try:
            db = client[self.database_name]
            
            db.create_collection(collection_name)
            client.close()
            return True
        
        except CollectionInvalid as e:
            print('Collection creation error:', str(e))
            return False
    
        except PyMongoError as e:
            print('An error occurred:', str(e))
            return False


    def query_with_timeout(self, client: MongoClient, timeoutms:float, query: dict) -> list:
        try:
            db = client[self.database_name]
            collection = db[self.collection_name]

            query_options = {'$query': query, '$maxTimeMS': timeoutms}

            result = list(collection.find(query_options))
            return result
        except ExecutionTimeout as e:
            print('Query execution timeout:', str(e))
            return []
    
        except PyMongoError as e:
            print('An error occurred:', str(e))
            return []
        


    def update_document(self, client: MongoClient, filter_query: dict, update_query:dict)-> bool:
        try:
            db = client[self.database_name]
            collection = db[self.collection_name]

            result = collection.update_one(filter_query, update_query)

            if result.modified_count > 0:
                return True
            else:
                return False

        except OperationFailure as e:
            print('Operation failure:', str(e))
            return False
    
        except PyMongoError as e:
            print('An error occurred:', str(e))
            return False


x = Base()
x.adress = "127.0.0.1"
x.port = "27017"

client = x.connect_to_db()

if client is not None:
    print("Connected to MongoDB successfully.")
else:
    print("Failed to connect to MongoDB.")

x.database_name = 'test'
x.collection_name = 'testukas'

query = x.query_databases(client=client, value='trout')

if query[1] is False:
    print(f"Failed to query: {query}")
else:
    print(query)

print(x.create_collection(collection_name='Naujas'))

query = {'name': 'trout'}
print(x.query_with_timeout(client=client, timeoutms=0.9, query=query))


update = {'$sett': {'quantity': "100"}}
print(x.update_document(client=client, filter_query=query, update_query=update))