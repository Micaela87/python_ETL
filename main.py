from CDC import Cdc
from Db.db import DbConfig
from Functions.etl import etl_process

if __name__ == "__main__":
    
    client = DbConfig()
    connects = client.test_connection()
    
    if connects:
        client.connect()
        cdc = Cdc()
        cdc.track_collection_changes("users")
        etl_process()