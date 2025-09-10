from kafka import KafkaProducer

class KafkaProducerConnection:

    def __init__(self, configs : dict) -> None:
        self.configs = configs
        self.producer = None


    def __enter__(self):
        self.open()
        return self.producer


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        if exc_type is not None:
            print(f"An exception occurred: {exc_val}")
        return False


    def open(self):
        self.producer = KafkaProducer(**self.configs)


    def close(self):
        if self.producer:
            self.producer.close()
            self.producer = None