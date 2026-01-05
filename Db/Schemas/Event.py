from typing import NotRequired, Required, TypedDict
from datetime import datetime
from db import db

collection = db["events"]

class Event(TypedDict):
    name: Required[str]
    owner: Required[str]
    action: NotRequired[str]
    callback: NotRequired[str]
    processed: Required[bool]
    date: Required[datetime]
    version: Required[int]
    createdAt: Required[datetime]