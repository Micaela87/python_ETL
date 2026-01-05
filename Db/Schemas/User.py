from typing import NotRequired, Required, TypedDict
from datetime import datetime
from db import db

collection = db["users"]

class User(TypedDict):
    firstName: Required[str]
    lastName: Required[str]
    email: Required[str]
    password: Required[str]
    dateOfBirth: NotRequired[datetime]