from pathlib import Path

class DataBuilder:

    @staticmethod
    def metadata_to_dict(file_path_object : Path) -> dict:
        return {
            'file_path' : str(file_path_object),
            'file_name' : file_path_object.name,
            'file_size' : file_path_object.stat().st_size,
            'last_modified_time' : file_path_object.stat().st_mtime,
            'creation_time' : file_path_object.stat().st_ctime
        }