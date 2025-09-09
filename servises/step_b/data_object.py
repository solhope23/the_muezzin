class DataObject:

    def __init__(self, file, file_name, file_size, last_modified_time, creation_time):
        self.file = file
        self.file_name = file_name
        self.file_size = file_size
        self.last_modified_time = last_modified_time
        self.creation_time = creation_time


    def str_time_to_datatime(self):


        # The string to be converted
        datetime_string = "2025-09-09 17:58:00.123456"

        # The format string matching the input string's format
        format_string = "%Y-%m-%d %H:%M:%S.%f"

        # Convert the string back to a datetime object
        datetime_object = datetime.strptime(datetime_string, format_string)

