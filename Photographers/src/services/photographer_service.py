from src.services.photographerRepository import PhotographerRepository


class PhotographerService:

    def __init__(self, repository: PhotographerRepository):
        self.repository = repository


    def get_all_photographers(self):
        return self.repository.get_all_photographers()

    def get_photographer_by_id(self, id):
        return self.repository.get_photographer_by_id(id)

    def get_photographer_by_event_type(self, event_type):
        return self.repository.get_photographer_by_event_type(event_type)


