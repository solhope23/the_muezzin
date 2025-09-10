import os
import json
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from pymongo.mongo_client import MongoClient
from gridfs import GridFSBucket
from datetime import datetime
import hashlib

# CONFIGS

# kafka_configs
my_consumer_configs =  {
                'bootstrap_servers': [os.getenv("kafka_uri", "localhost:9092")],
                'group_id': "my-consumer",
                'auto_offset_reset': "earliest",
                'enable_auto_commit': 'True',
                'value_deserializer': lambda v: json.loads(v.decode("utf-8"))
            }
topic_name = 'podcasts_metadata'
#


# elasticsearch_configs
es_uri = os.getenv("elastic_uri", "http://localhost:9200")

index_name = "podcasts_metadata"

mapping = {
    "mappings": {
        "properties": {
            "file_name": {
                "type": "keyword"
            },
            "file_size": {
              "type" : "long"
            },
            "last_modified_time": {
                "type": "date",
                "format": "yyyy-MM-dd HH:mm:ss.SSSSSS"
            },
            "creation_time": {
                "type": "date"
            }
        }
    }
}
#

# mongodb_configs
my_mongodb_uri = os.getenv("mongodb_uri", "mongodb://localhost:27017")

db_name = "the_muezzin"

col_name = "podcasts_metadata"
#
#


# OBJECTS

consumer = KafkaConsumer(topic_name, **my_consumer_configs)

es = Elasticsearch(es_uri)

my_client = MongoClient(my_mongodb_uri)

fs = GridFSBucket(my_client[db_name], col_name)


#
#

# LOGIC

# read_from_kafka
for consumer_message in consumer:
    message = consumer_message.value

    # convert back strTime to_datatime
    format_string = "yyyy-MM-dd HH:mm:ss.SSSSSS"

    message["last_modified_time"] = datetime.strptime(message["last_modified_time"], format_string)
    message["creation_time"] = datetime.strptime(message["creation_time"], format_string)

    # create_unique_id
    unique_key = f"{message["file_name"]} {message["file_size"]} {message["creation_time"]}"
    unique_id = hashlib.sha1(unique_key.encode()).hexdigest()

    # Reading the audio file in bits
    with open(message["file_path"], "rb") as f:
        file_audio = f.read()

    # Create a document for elasticsearch
    doc_for_elasticsearch = {
        'file_name' : message["file_name"],
        "file_size" : message["file_size"],
        "last_modified_time" : message["last_modified_time"],
        "creation_time" : message["creation_time"]
    }

    # Create index in elastic if not exists:

    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, body=mapping)

    # index doc
    es.index(index=index_name, id=unique_id, document=doc_for_elasticsearch)

    # insert podcast to mongodb
    file_id = fs.open_upload_stream_with_id(unique_id, message["file_name"])
    file_id.write(file_audio)
    file_id.close()