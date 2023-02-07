import pika 

def minha_callback(ch, method, properties, body):
    print(body)
    # print(type(body))


queue = 'data_queue'
connection_parameters = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    credentials=pika.PlainCredentials(
        username='guest',
        password='guest'
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()
channel.queue_declare(
    queue=queue,
    durable=True
)

channel.basic_consume(
    queue=queue,
    auto_ack=True,
    on_message_callback=minha_callback
)

print(f'Listen RabbitMQ on port 5672')
channel.start_consuming()