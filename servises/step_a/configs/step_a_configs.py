import os
import json

class StepAConfigs:

        data_directory_path = os.getenv("DATA_DIRECTORY_PATH", "data\podcasts")
        kafka_host = os.getenv("KAFKA_HOST", "localhost")
        kafka_port = os.getenv("KAFKA_PORT", 9092)
        topic = os.getenv("KAFKA_TOPIC", 'podcasts_metadata')

        @classmethod
        def get_kafka_configs(cls):
            return {
                'bootstrap_servers': [f"{cls.kafka_host}:{cls.kafka_port}"],
                'value_serializer': lambda v: json.dumps(v).encode("utf-8")
            }