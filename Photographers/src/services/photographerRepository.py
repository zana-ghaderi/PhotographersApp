from typing import List

from src.database.cache import get_redis_client
from src.database.cassandra import get_cassandra_session
from src.models.photographer import Photographer
from src.models.photographer_respnse import PhotographerResponse


class PhotographerRepository:
    def __init__(self, photographers: List[Photographer]):
        self.photographers = photographers
        self.cassandra = get_cassandra_session()
        self.redis = get_redis_client()

    def get_all_photographers(self):
       # photographers = self.redis.get('all_photographer')
        return [self._to_response(photographer) for photographer in self.photographers]

    def get_photographer_by_id(self, photographer_id):
        photographer = [p for p in self.photographers if p.id == photographer_id]
        return self._to_response(photographer[0])

    def get_photographer_by_event_type(self, event_type):
        return [self._to_response(photographer) for photographer in self.photographers if event_type in photographer.event_type.type]

    def _to_response(self, photographer: Photographer):
        return PhotographerResponse(
            id = photographer.id,
            uid = photographer.uid,
            first_name=photographer.first_name,
            last_name=photographer.last_name,
            address=photographer.address,
            event_type=photographer.event_type
        )