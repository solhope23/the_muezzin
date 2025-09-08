from project.servises.retriever.configs.retriever_configs import RetrieverConfigs
from project.classes.dal.readers.file_reader import FileReader
from project.classes.data_builder.data_builder import DataBuilder
from project.classes.dal.writers.my_kafka_producer.my_kafka_producer import MyKafkaProducer



class RetrieverManager:

    def __init__(self):
        self.peth_object_files = FileReader.get_path_object_of_file(RetrieverConfigs.data_directory_path)
        self.topic_name = RetrieverConfigs.retriever_topic
        self.producer = MyKafkaProducer(RetrieverConfigs.configs_producer)


    def retriever(self):
        try:
            dict_metadata = DataBuilder.generator_metadata_to_dict(self.peth_object_files)
            for massage in dict_metadata:
                self.producer.open()
                self.producer.send_to_kapka(self.topic_name, massage)
        except Exception as e:
            print(type(e).__name__, "-", e)
        finally:
            self.producer.close()






