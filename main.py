from CDC.Cdc import Cdc
from Db.db import DbConfig
from Functions.etl import etl_process

if __name__ == "__main__":
    
    instance = DbConfig()
    connects = instance.test_connection()
    
    if connects:
        client = instance.client
        instance.connect()
        cdc = Cdc(client)
        cdc.track_collection_changes("users")
        etl_process()