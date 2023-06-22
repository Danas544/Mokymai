class Base:
    def __init__(self, db:str ) -> Any:
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db]

    def get_db(self):
        return self.db
    
    @staticmethod
    def sum_price_from_documents(documents)-> float:
        price_list = [ document['price'] for document in documents]
        sum_pice = round(sum(map(float, price_list)),2)
        return sum_pice
    
    @staticmethod
    def average_price_from_documents(list_price: list) -> float:
        return round(sum(list_price) / len(list_price),2)

    def get_collection_names(self) -> list[str]:
        return self.db.list_collection_names()




class Collections(Base):
    def __init__(self, db: str ,collection: str = None) -> Any:
        super().__init__(db = db)
        self.db = self.get_db()
        if collection is not None:
            self.collection = self.db[collection]
        else:
            pass