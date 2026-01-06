from CDC.Cdc import Cdc
from Db.db import DbConfig
from Services.ETLService import ETLService

if __name__ == "__main__":
    
    db_instance = DbConfig()
    connects = db_instance.test_connection()
    
    if connects:
        client = db_instance.client
        db_instance.connect()
        cdc_instance = Cdc(client)
        cdc_instance.track_collection_changes("users")
        
        etl_instance = ETLService()
        etl_instance.process_data()