
from pydantic import BaseModel

from src.models.photographer import Address, EventType


class PhotographerResponse(BaseModel):
    id: int
    uid: str
    first_name: str
    last_name: str
    event_type: EventType
    address: Address

