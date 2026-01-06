import datetime
import logging
import pymongo
from CDC.RabbitMQ.RabbitMQService import RabbitMQService
from Db.Schemas.Event import Event

class Cdc():

    client = None
    db = None
    rabbitmq_service = None

    def __init__(self, client):
        self.client = client
        self.db = client["test"]
        self.rabbitmq_service = RabbitMQService()

    def track_collection_changes(self, collection_name):
        try: 
            resume_token = None
            collection = self.db[collection_name]
            with collection.watch() as stream:
                logging.info(f"Watching collection '{collection_name}' for changes...")
                self.rabbitmq_service.create_queue()
                for change in stream:
                    logging.info(f"Change detected: Operation Type: {change['operationType']}")
                    self.handle_collection_changes(change)
        except pymongo.errors.PyMongoError as e:
            if resume_token is None:
                logging.error(f"An unrecoverable error occurred: {e}")
            else:
                with collection.watch(resume_after = resume_token) as stream:
                    logging.info(f"Resuming collection watching '{collection_name}' for changes...")
                    for change in stream:
                        logging.info(f"Change detected: Operation Type: {change['operationType']}")
                        self.handle_collection_changes(change)
        except KeyboardInterrupt:
            logging.info("Change stream closed by user.")
        finally:
            if self.client:
                self.client.close()

    def handle_collection_changes(self, change):
        event = Event()
        match change['operationType']:
            case "insert":
                event["name"] = change['operationType']
                event["owner"] = change["documentKey"]["_id"]
                event["action"] = ""
                event["callback"] = ""
                event["processed"] = False
                event["date"] = change["wallTime"]
                event["version"] = 1
                event["createdAt"] = datetime.datetime.now()

                self.db.events.insert_one(event)
                self.rabbitmq_service.send_massage(change['operationType'])

            case 'update':
                event["name"] = change['operationType']
                event["owner"] = change["documentKey"]["_id"]
                event["action"] = ""
                event["callback"] = ""
                event["processed"] = False
                event["date"] = change["wallTime"]
                event["version"] = 1
                event["createdAt"] = datetime.datetime.now()

                self.db.events.insert_one(event)
                self.rabbitmq_service.send_massage(change['operationType'])

            case 'delete':
                event["name"] = change['operationType']
                event["owner"] = change["documentKey"]["_id"]
                event["action"] = ""
                event["callback"] = ""
                event["processed"] = False
                event["date"] = change["wallTime"]
                event["version"] = 1
                event["createdAt"] = datetime.datetime.now()

                self.db.events.insert_one(event)
                self.rabbitmq_service.send_massage(change['operationType'])