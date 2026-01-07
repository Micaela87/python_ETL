import logging
import pika
from Services.ETLService import ETLService
from Db.db import DbConfig

class RabbitMQService():

    connection = None
    channel = None

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()

    def create_queue(self):
        self.channel.queue_declare(queue='events')

    def send_massage(self, body):
        self.channel.basic_publish(
            exchange = '',
            routing_key = 'events',
            body = body)
        print(f"Sent {body}")
        logging.info(f"Sent {body}")

    def get_message(self, client):

        def cb(ch, method, properties, body):
            print(f"Received {body}")
            etl_instance = ETLService(client)
            etl_instance.process_data(body.decode('ascii'))

        self.channel.queue_declare(queue='events')
        self.channel.basic_consume(queue='events',
                      auto_ack=True,
                      on_message_callback=cb)
        self.channel.start_consuming()
        