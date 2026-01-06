from typing import TypedDict
from datetime import datetime

class Event(TypedDict):
    name: str
    owner: str
    action: str
    callback: str
    processed: bool
    date: datetime
    version: int
    createdAt: datetime