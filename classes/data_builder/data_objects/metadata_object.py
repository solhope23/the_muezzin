from pathlib import Path

class MetaData:

    def __init__(self, file_path_object : Path) -> None:
        self.file_path = str(file_path_object)
        self.file_name = file_path_object.name
        self.file_size = file_path_object.stat().st_size
        self.last_modified_time = file_path_object.stat().st_mtime
        self.creation_time = file_path_object.stat().st_ctime



    def get_metadata_dict(self) -> dict:
        return self.__dict__