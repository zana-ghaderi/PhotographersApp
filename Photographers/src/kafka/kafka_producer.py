from confluent_kafka import Producer, KafkaError

import json

from src.config.config import KAFKA_CONFIG


class KafkaProducer:
    def __init__(self):
        self.producer = Producer(**KAFKA_CONFIG)

    def delivery_report(self, err, msg):
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    def send_message(self, topic, message):
        try:
            self.producer.produce(topic,
                                  json.dumps(message).encode('utf-8'),
                                  callback=self.delivery_report)
            self.producer.poll(0)
        except KafkaError as e:
            print(f'Error producing message: {e}')

    def flush(self):
        self.producer.flush()