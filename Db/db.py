import logging
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

load_dotenv()

class DbConfig():

    connection_string: str = None
    client: MongoClient = None
    db: str = None

    def __init__(self):
        self.connection_string = os.getenv("DB_CONNECTION_STRING")

    def connect(self):
        self.client = MongoClient(self.connection_string)
        self.db = self.client["dev"]


    def test_connection(self):
        try:
            self.client = MongoClient(self.connection_string)
            self.client.admin.command('ping')
            logging.info("MongoDB server is reachable and connected!")
            return True
        except ConnectionFailure as e:
            logging.error(f"{e}")
            return False


