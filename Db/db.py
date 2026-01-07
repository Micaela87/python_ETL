import logging
import os
from dotenv import load_dotenv
import pymongo

load_dotenv()

class DbConfig():

    connection_string: str = None
    client = None
    db: str = None

    def __init__(self):
        self.connection_string = os.getenv("DB_CONNECTION_STRING")

    def connect(self):
        self.client = pymongo.MongoClient(self.connection_string)
        self.db = self.client["test"]


    def test_connection(self):
        try:
            self.client = pymongo.MongoClient(self.connection_string)
            self.client.admin.command('ping')
            print("Successfully connected to MongoDb")
            logging.info("MongoDB server is reachable and connected!")
            return True
        except pymongo.errors.ConnectionFailure as e:
            logging.error(f"{e}")
            return False


