import os
from project.classes.configs.configs import Configs

class MongoDBConfigs:


    scheme = os.getenv("HOST", "mongodb")
    user_name = os.getenv("USER_NAME")
    password = os.getenv("PASSWORD")
    host = os.getenv("HOST", "localhost")
    port = os.getenv("PORT", "27017")
    db = os.getenv("DATABASE", "the_muezzin")
    query_parameters = os.getenv("QUERY_PARAMETERS")
    collection = os.getenv("COLLECTION", "podcasts_metadata")
    uri = Configs.uri_builder(
        scheme=scheme,
        user_name=user_name,
        password=password,
        host=host,
        port=port,
        path=db,
        query_parameters=query_parameters
    )


