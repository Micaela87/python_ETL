from datetime import datetime
import logging

class User():
    
    firstName = None
    lastName = None
    email = None
    password = None
    dateOfBirth = None

    def __init__(self, user):

        self.firstName = user["firstName"]
        self.lastName = user["lastName"]
        self.email = user["email"]
        self.password = user["password"]
        self.dateOfBirth = user["dateOfBirth"]

    async def insert_user(self, client):

        try: 

            db = client["test"]
            #collection = db.users
            
            return await db.users.insert_one({
                "firstName": self.firstName,
                "lastName": self.lastName,
                "email": self.email,
                "password": self.password,
                "dateOfBirth": self.dateOfBirth
            })
        
        except Exception as e:
            print(f"An error occurred: {e}")
            logging.info(f"An error occurred: {e}")
        