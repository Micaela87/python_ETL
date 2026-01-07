import datetime
import logging
import dotenv
from pyspark.sql import SparkSession

from Db.db import DbConfig

dotenv.load_dotenv()

class ETLService():

    client = None
    db = None
    spark = None

    def __init__(self, client):
        self.client = client
        self.db = client["test"]
        self.spark = SparkSession \
            .builder \
            .appName("ETL") \
            .getOrCreate()

    def extract_data(self, message):
        collection = self.db["events"]
        cursor = collection.find({ "name": message, "processed": False })
        return list(cursor)

    def transform_data(self, message, data):

        filter = { "name": message, "processed": False }
        update = {
            "$set": { "processed": True, "date": datetime.datetime.now() },
        }

        self.db.events.update_many(filter, update)

        for item in data:
            item["_id"] = str(item["_id"])
            item["owner"] = str(item["owner"])

        df = self.spark.createDataFrame(data)
        return data


    def load_data(self, event, data):
        return self.db.analytics.insert_one({
            "event": event,
            "processed": True,
            "quantity": len(data),
            "date": datetime.datetime.now()
        })

    def process_data(self, message):
        try:
            events_list = self.extract_data(message)
            data = self.transform_data(message, events_list)
            self.load_data(message, data)
        except Exception as e:
            print(f"{e}")
            logging.error(f"An error occurred: {e}")
