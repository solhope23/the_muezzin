from project.classes.dal.readers.file_reader import FileReader
from project.classes.data_builder.data_builder import DataBuilder
from project.classes.dal.writers.my_kafka_producer.my_kafka_producer import MyKafkaProducer
from project.servises.retriever.configs.retriever_configs import RetrieverConfigs


class RetrieverManager:

    def __init__(self, producer, massages_gen):
        self.configs = RetrieverConfigs().get_dict_configs()
        self.peth_files = self.configs["data_directory_path"]
        self.topic_name = self.configs["producer_topic"]
        self.producer = MyKafkaProducer(**self.configs["configs_producer"])

