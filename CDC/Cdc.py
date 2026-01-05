import logging
from pymongo.errors import PyMongoError
from Db.Schemas.Event import Event

class Cdc():

    def track_collection_changes(self, collection_name):
        try: 
            resume_token = None
            collection = self.db[collection_name]
            with collection.watch() as stream:
                logging.info(f"Watching collection '{collection_name}' for changes...")
                for change in stream:
                    logging.info(f"Change detected: Operation Type: {change['operationType']}")
                    self.handle_collection_changes(change)
        except PyMongoError as e:
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

    def handle_collection_changes(change):
        event = Event()
        match change['operationType']:
            case "insert":
                logging.info(f"{change}")
                return change
                # event.name: change['operationType']
                # event.owner: Required[str]
                # event.action: NotRequired[str]
                # event.callback: NotRequired[str]
                # event.processed: Required[bool]
                # event.date: Required[datetime]
                # event.version: Required[int]
                # event.createdAt: Required[datetime]
            case 'update':
                logging.info(f"{change}")
                return change
            case 'delete':
                logging.info(f"{change}")
                return change