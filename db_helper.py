import pymongo
import json

class DbHelper:

    def __init__(self, db: str):
        self.client = self.connection()
        self.db = self.client[db]



    def connection(self) -> pymongo.MongoClient:
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        return client


    def add_single_data(self, data: str, collection: str) -> None:
        collection = self.db[collection]
        collection.insert_one(data)


    def clear_collection(self, collection: str) -> None:
        collection = self.db[collection]
        collection.delete_many({})


    def get_all_data(self, collection: str) -> json:
        collection = self.db[collection]
        data = collection.find()
        return data