import os
import json

class RetrieverConfigs:

    def __init__(self):
        self.data_directory_path = os.getenv("DATA_DIRECTORY_PATH", "data\podcasts")
        self.producer_host = os.getenv("KAFKA_PRODUCER_HOST", "localhost")
        self.producer_port = os.getenv("KAFKA_PRODUCER_PORT", 9092)
        self.producer_topic = os.getenv("KAFKA_PRODUCER_TOPIC", 'podcasts_metadata')
        self.configs_producer = {
            'bootstrap_servers':[f"{self.producer_host}:{self.producer_port}"],
            'value_serializer': lambda v: json.dumps(v).encode("utf-8")
        }


    def get_dict_configs(self):
        return self.__dict__

