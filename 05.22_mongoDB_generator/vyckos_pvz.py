from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from typing import Dict, List, Any, Optional

class TaskManager:
    def __init__(
        self, host: str, port: int, db_name: str, collection_name: str
    ) -> None:
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def create_task(self, task: Dict[str, Any]) -> str:
        result = self.collection.insert_one(task)
        return str(result.inserted_id)

    def get_all_tasks(self) -> List[Dict[str, Any]]:
        return list(self.collection.find())

    def get_task(self, task_name: str) -> Dict[str, Any]:
        return list(self.collection.find({"task_name": task_name}))

    def update_task(self, task_name: str, task_updates: Dict[str, Any]) -> bool:
        result = self.collection.update_one(
            {"task_name": task_name}, {"$set": task_updates}
        )
        return result.modified_count > 0

    def delete_task(self, task_name: str) -> bool:
        result = self.collection.delete_one({"task_name": task_name})
        return result.deleted_count > 0

    def get_single_querry(
        self, querry: Dict[str, Any], fields: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        return self.collection.find_one(querry, fields)

db = TaskManager(    host = 'localhost',
    port = 27017,
    db_name = 'mydatabase',
    collection_name = 'mycollection')

# db.create_task({"pirmas_mano_mongo_task": 1,
#                 "trecias_mano_mongo_task": 3})

print(db.get_task("trecias_mano_mongo_task"))



# print(db.get_all_tasks())