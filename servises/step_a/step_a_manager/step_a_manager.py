from project.servises.step_a.configs.step_a_configs import StepAConfigs
from project.classes.dal.connections.kafka_producer_connection import KafkaProducerConnection
from project.classes.dal.readers.file_reader import FileReader
from project.classes.data_builder.data_builder import DataBuilder
from project.classes.dal.writers.my_kafka_producer.my_kafka_producer import MyKafkaProducer


class StepAManager:

    def __init__(self):
        self.data_directory_path = StepAConfigs.data_directory_path
        self.topic_name = StepAConfigs.retriever_topic
        self.configs_producer = StepAConfigs.configs_producer


    def manage(self):
        try:
            gen_files_path_object = FileReader.read_file_path_object_gen(self.data_directory_path)
            gen_metadata_objects = DataBuilder.gen_metadata_to_metadata_object(gen_files_path_object)
            with KafkaProducerConnection(self.configs_producer) as kafka_client:
                producer = MyKafkaProducer(kafka_client)
                for metadata_object in gen_metadata_objects:
                    massage = metadata_object.get_metadata_dict()
                    producer.send_to_kapka(self.topic_name, massage)
        except Exception as e:
            print(type(e).__name__, "-", e)






