from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["your_database"]
collection = db["your_collection"]
filter = {"level1.level2.level3": "value_to_match"}
update = {"$set": {"level1.level2.$.level3": "new_value"}}
collection.update_many(filter, update)
