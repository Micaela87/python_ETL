from typing import TypedDict
from datetime import datetime

class User(TypedDict):
    firstName: str
    lastName: str
    email: str
    password: str
    dateOfBirth: datetime