import os
import json
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from pymongo.mongo_client import MongoClient
from gridfs import GridFSBucket

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
my_elastic_uri = os.getenv("elastic_uri", "http://localhost:9200")

index_name = "podcasts_metadata"
#

# mongodb_configs
my_mongodb_uri = os.getenv("mongodb_uri", "mongodb://localhost:27017")

db_name = "the_muezzin"

col_name = "podcasts_metadata"
#

# OBJECTS












consumer = KafkaConsumer()
es = Elasticsearch(os.getenv("elastic_search_"))