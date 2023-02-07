from typing import Dict
import pika
import json

class RabbitmqPublisher:
    def __init__(self) -> None:
        self.__host = 'localhost'
        self.__port = 5672
        self.__username = 'guest'
        self.__password = 'guest'
        self.__exchange = "data_exchange"
        self.__routing_key = ''
        self.__channel = self.__create_channel()
    
    def __create_channel(self):
        connection_parameter = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pika.BlockingConnection(connection_parameter).channel()
        return channel
    
    def sendMessage(self, body:Dict):
        self.__channel.basic_publish(
            exchange=self.__exchange,
            routing_key=self.__routing_key,
            body=json.dumps(body),
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )

rabbitmqPublisher = RabbitmqPublisher()
rabbitmqPublisher.sendMessage({'ola':'mundo'})
