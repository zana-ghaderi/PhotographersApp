from pydantic import BaseModel
from typing import List


class Address(BaseModel):
    city: str
    street_name: str
    street_address: str
    zip_code: str
    state: str
    country: str


class EventType(BaseModel):
    type: List[str]


class Photographer(BaseModel):
    id: int
    uid: str
    first_name: str
    last_name: str
    event_type: EventType
    address: Address
