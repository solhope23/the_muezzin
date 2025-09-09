from pymongo import MongoClient
from gridfs import GridFSBucket


class MongoDBFetcher:


    def __init__(self, client : MongoClient, db_name : str, col_name : str) -> None:
        self.client = client
        self.db_name = db_name
        self.col_name = col_name
        self.fs = GridFSBucket(client[db_name], col_name)


    def write_file_with_gridfs(self, is_id, file_name, file):
        try:
            file_id = self.fs.open_upload_stream_with_id(is_id, file_name)
            file_id.write(file)
            file_id.close()
        except Exception as e:
            print(type(e).__name__, "-", e)







