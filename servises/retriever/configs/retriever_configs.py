import os
import json

class RetrieverConfigs:

        data_directory_path = os.getenv("DATA_DIRECTORY_PATH", "data\podcasts")
        kafka_host = os.getenv("KAFKA_HOST", "localhost")
        kafka_port = os.getenv("KAFKA_PORT", 9092)
        retriever_topic = os.getenv("KAFKA_TOPIC", 'podcasts_metadata')
        configs_producer = {
            'bootstrap_servers':[f"{kafka_host}:{kafka_port}"],
            'value_serializer': lambda v: json.dumps(v).encode("utf-8")
        }