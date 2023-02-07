import pika

connection_parameter = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials(
        username='guest',
        password='guest'
    )
)

channel = pika.BlockingConnection(connection_parameter).channel()

channel.basic_publish(
    exchange="data_exchange",
    routing_key='',
    body="Alguma coisa",
    properties=pika.BasicProperties(
        delivery_mode=2
    )
)

