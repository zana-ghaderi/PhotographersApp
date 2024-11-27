import pytest
from unittest.mock import MagicMock
from src.services.photographer_service import PhotographerService
from src.models.photographer import Photographer, Address, EventType


@pytest.fixture()
def sample_photographers():
    return [
        Photographer(
            id=3391,
            uid="e70098c4-ffe4-4c57-a508-c9f3d1a93822",
            first_name="Karey",
            last_name="Kuhic",
            address=Address(city="", street_name="", street_address="", zip_code="", state="", country=""),
            event_type=EventType(type=["birthday", "wedding"])
        ),
        Photographer(
            id=3392,
            uid="e70098c4-ffe4-4c57-a508-c9f3d1a93822",
            first_name="Willia",
            last_name="Rowe",
            address=Address(city="", street_name="", street_address="", zip_code="", state="", country=""),
            event_type=EventType(type=["wildlife", "wedding"])
        )
    ]


@pytest.fixture()
def photographer_service(sample_photographers):
    mock_repository = MagicMock()
    mock_repository.get_all_photographers.return_value = sample_photographers
    mock_repository.get_photographer_by_id.return_value = next(p for p in sample_photographers if p.id == 3392)
    mock_repository.get_photographer_by_event_type.return_value = [p for p in sample_photographers if
                                                                   "wedding" in p.event_type.type]

    return PhotographerService(repository=mock_repository)


def test_get_all_photographers(photographer_service):
    photographers = photographer_service.get_all_photographers()
    assert len(photographers) == 2
    assert photographers[0].first_name == "Karey"


def test_get_photographer_by_id(photographer_service):
    photographer = photographer_service.get_photographer_by_id(3392)
    assert photographer.last_name == "Rowe"


def test_get_photographer_by_event_type(photographer_service):
    photographers = photographer_service.get_photographer_by_event_type("wedding")
    assert len(photographers) == 2
