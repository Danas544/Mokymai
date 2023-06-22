from pymongo import MongoClient
from pymongo.errors import OperationFailure

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["exercise_db"]
collection = db["exercise_collection"]

# Define the validation rules as a dictionary
validation_rules = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "age", "email"],
            "properties": {
                "name": {"bsonType": "string"},
                "age": {"bsonType": "int", "minimum": 18, "maximum": 99},
                "email": {
                    "bsonType": "string",
                    "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                },
            },
        }
    }
}

# Set the validation rules for the collection
try:
    db.create_collection('exercise_collection')
except:
    pass
try:
    db.command("collMod", collection.name, **validation_rules)
    print("Schema validation enabled.")
except OperationFailure as e:
    print(f"Failed to enable schema validation: {e}")

# Insert documents
valid_doc = {"name": "John Doe", "age": 25, "email": "johndoe@example.com"}
invalid_doc1 = {"name": "Jane Smith", "age": "25", "email": "janesmith"}
invalid_doc2 = {"name": 123, "age": 35, "email": "invalid_email"}

collection.insert_one(valid_doc)
collection.insert_one(invalid_doc1)
collection.insert_one(invalid_doc2)


# Print all documents
documents = collection.find()
for doc in documents:
    print(doc)

# Clean up
collection.drop()
client.close()
