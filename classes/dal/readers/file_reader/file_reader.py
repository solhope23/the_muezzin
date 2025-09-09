from pathlib import Path

class FileReader:

    @staticmethod
    def read_file_path_object_gen(file_directory_path):
        for file_path in Path(file_directory_path).iterdir():
            if Path(file_path).is_file():
                yield Path(file_path)


    @staticmethod
    def read_binary_audio_file(path):
        with open(path, "rb") as f:
            return f.read()


