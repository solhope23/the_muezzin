from pathlib import Path

class FileReader:

    @staticmethod
    def get_path_object_of_file(directory_path):
        for file_path in Path(directory_path).iterdir():
            if Path(file_path).is_file():
                yield Path(file_path)