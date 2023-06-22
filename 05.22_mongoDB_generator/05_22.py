from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List

def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database

def insert_document(collection: Collection, document: Dict) -> str:
    result = collection.insert_one(document)
    return str(result.inserted_id)

def find_documents(collection: Collection, query: Dict) -> List[Dict]:
    documents = collection.find(query)
    return list(documents)

def update_document(collection: Collection, query: Dict, update: Dict) -> int:
    result = collection.update_many(query, {"$set": update})
    return result.modified_count


def delete_documents(collection: Collection, query: Dict) -> int:
    result = collection.delete_many(query)
    return result.deleted_count

def list_databases(client: MongoClient) -> List[str]:
    return client.list_database_names()

def list_collections(database: Database) -> List[str]:
    return database.list_collection_names()

# Example usage
if __name__ == "__main__":
    # Connection details
    mongodb_host = 'localhost'
    mongodb_port = 27017
    database_name = 'mydatabase'
    collection_name = 'mycollection'

    # Connect to MongoDB
    client = MongoClient(mongodb_host, mongodb_port)
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    # Retrieve a specific collection
    collection = db[collection_name]

    # Create (Insert) Operation
    document = {
        "name": "John Doe",
        "age": 30,
        "email": "johndoe@example.com"
    }
    inserted_id = insert_document(collection, document)
    print(f"Inserted document with ID: {inserted_id}")

    query = {"name": "John Doe"}
    results = find_documents(collection, query)
    print("Matching documents:")
    for result in results:
        print(result)

        # List all databases
    databases = list_databases(client)
    print("List of databases:")
    for db_name in databases:
        print(db_name)

    # List collections in the connected database
    collections = list_collections(db)
    print("Collections in the connected database:")
    for collection_name in collections:
        print(collection_name)