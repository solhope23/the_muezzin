from elasticsearch import Elasticsearch


class ElasticSearchConnection:


    def __init__(self, uri : str) -> None:
        self.uri = uri
        self.elastic_search = None


    def __enter__(self):
        self.elastic_search = Elasticsearch(self.uri)
        return self.elastic_search


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.elastic_search:
            self.elastic_search.close()
        if exc_type is not None:
            print(f"An exception occurred: {exc_val}")


    def open(self) -> None:
        self.elastic_search = Elasticsearch(self.uri)


    def close(self) -> None:
        if self.elastic_search:
            self.elastic_search.close()
        self.elastic_search = None