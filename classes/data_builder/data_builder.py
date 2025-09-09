from project.classes.data_builder.data_objects.metadata_object import MetaData
import hashlib


class DataBuilder:


    @staticmethod
    def gen_metadata_to_metadata_object(gen_files_path_object):
        for file_path_object in gen_files_path_object:
            metadata_object = MetaData(file_path_object)
            yield metadata_object


    @staticmethod
    def create_unique_id(*values_for_hash):
        result_values = "_".join(str(val) for val in values_for_hash)
        return hashlib.sha1(result_values.encode()).hexdigest()


    @staticmethod
    def gen_bulk_doc_builder(docs_gen, index, is_id = None):
        for doc in docs_gen:
            item = {"_index": index, "_source": doc}
            if is_id:
                item['_id'] = is_id
            yield item