import pika

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
        print(f" [x] Sent {body}")