from datetime import datetime
import hashlib

class DataObject:

    def __init__(self, file, file_name, file_size, last_modified_time, creation_time):
        self.file = file
        self.file_name = file_name
        self.file_size = file_size
        self.last_modified_time = last_modified_time
        self.creation_time = creation_time
        self.unique_id = DataObject.create_unique_id(file_name,file_size)


    def str_time_to_datatime(self):
        format_string = "%Y-%m-%d %H:%M:%S.%f"
        self.last_modified_time = datetime.strptime(self.last_modified_time, format_string)
        self.creation_time = datetime.strptime(self.creation_time, format_string)

    @staticmethod
    def create_unique_id(*values_for_hash):
        result_values = "_".join(str(val) for val in values_for_hash)
        return hashlib.sha1(result_values.encode()).hexdigest()


    def get_metadata(self):
        return {
            'id'
            'file_name' : self.file_name,
            'file_size' : self.file_size,
            'last_modified_time' : self.last_modified_time,
            'creation_time' : self.creation_time
        }

