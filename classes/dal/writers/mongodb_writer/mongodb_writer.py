import pymongo

class MongoDBFetcher:

    def __init__(self, client : pymongo):
        self.client = client


    def write(self, db_name, col_name, doc):
        self.client[db_name][col_name].insert_one(doc)
