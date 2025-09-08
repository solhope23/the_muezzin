from project.classes.data_builder.data_objects.metadata_object import MetaData


class DataBuilder:


    @staticmethod
    def generator_metadata_to_metadata_object(gen_files_path_object):
        for file_path_object in gen_files_path_object:
            metadata_object = MetaData(file_path_object)
            yield metadata_object