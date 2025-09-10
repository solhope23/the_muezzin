import os
import json

class KafkaConfigs:

        kafka_host = os.getenv("KAFKA_HOST", "localhost")
        kafka_port = os.getenv("KAFKA_PORT", "9092")
        topic = os.getenv("KAFKA_TOPIC", 'podcasts_metadata')
        group_id = os.getenv("GROUP_ID", "my-consumer")


        @classmethod
        def get_kafka_configs(cls):
            return {
                'bootstrap_servers': [f"{cls.kafka_host}:{cls.kafka_port}"],
                'group_id': cls.group_id,
                'auto_offset_reset': "earliest",
                'enable_auto_commit': 'True',
                'value_deserializer': lambda v: json.loads(v.decode("utf-8"))
            }
