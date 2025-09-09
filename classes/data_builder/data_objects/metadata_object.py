from pathlib import Path
from datetime import datetime

class MetaData:

    def __init__(self, file_path_object : Path) -> None:
        self.file_path = str(file_path_object)
        self.file_name = file_path_object.name
        self.file_size = file_path_object.stat().st_size
        self.last_modified_time = file_path_object.stat().st_mtime
        self.creation_time = file_path_object.stat().st_ctime
        self.timestamp_to_datetime()


    def timestamp_to_datetime(self) -> None:
        self.last_modified_time = datetime.fromtimestamp(self.last_modified_time)
        self.last_modified_time = self.last_modified_time.strftime("%Y-%m-%d %H:%M:%S.%f")
        self.creation_time = datetime.fromtimestamp(self.creation_time)
        self.creation_time = self.creation_time.strftime("%Y-%m-%d %H:%M:%S.%f")



    def get_metadata_dict(self) -> dict:
        return self.__dict__