from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class ElasticSearchIndexer:

    def __init__(self, client : Elasticsearch):
        self.client = client


    def create_index_by_mapping(self, index : str, mapping : dict) -> None:
        self.client.indices.create(index=index, body=mapping)


    def bulk_index(self, iter_docs) -> None:
        success, errors = bulk(self.client, iter_docs, raise_on_error=False)
        print(success)
        if errors:
            from pprint import pprint
            pprint(errors)
        print(success)