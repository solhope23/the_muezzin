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

    @staticmethod
    def generator_metadata_to_dict(gen_files_path_object):
        for file_path_object in gen_files_path_object:
            yield DataBuilder.metadata_to_dict(file_path_object)