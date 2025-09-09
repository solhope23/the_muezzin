from pymongo import MongoClient

class MongoDBFetcher:


    def __init__(self, client : MongoClient):
        self.client = client


    def write(self, db_name, col_name, doc):
        self.client[db_name][col_name].insert_one(doc)
