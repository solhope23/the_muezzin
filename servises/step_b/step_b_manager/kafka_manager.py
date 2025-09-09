from project.servises.step_b.configs.kafka_configs import KafkaConfigs
from project.classes.dal.connections.kafka_consumer_connection import KafkaConsumerConnection
from project.classes.dal.readers.my_kafka_concumer.my_kafka_consumer import MyKafkaConsumer

class KafkaManager:

    def __init__(self):
        self.configs = KafkaConfigs.get_kafka_configs()
        self.topic = KafkaConfigs.topic


    de