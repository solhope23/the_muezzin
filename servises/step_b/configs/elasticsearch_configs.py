import os
from project.classes.configs.configs import Configs

class ElasticSearchConfigs:


    scheme = os.getenv("HOST", "http")
    user_name = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST", "localhost")
    port = os.getenv("PORT", "9200")
    uri = Configs.uri_builder(
        scheme=scheme,
        user_name=user_name,
        password=password,
        host=host,
        port=port
    )
    index_name = os.getenv("INDEX_NAME", "podcasts_metadata")
