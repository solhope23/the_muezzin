from kafka import KafkaProducer

class MyKafkaProducer:

    def __init__(self, client : KafkaProducer) -> None:
        self.client = client


    def send_to_kapka(self, topic_name : str, data : dict) -> None:
        try:
            self.client.send(topic_name, data)
        except Exception as e:
            raise ValueError("Failed to send to Kapka") from e