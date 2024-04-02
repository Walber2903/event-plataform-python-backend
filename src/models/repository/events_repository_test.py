import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New register in database")
def test_insert_event():
  event = {
    "uuid": "my-uuid-show2",
    "title": "my title2",
    "slug": "my-slug-here2", 
    "maximum_attendees": 20,
  }

  events_repository = EventsRepository()
  response = events_repository.insert_event(event)
  print(response)

def test_get_event_by_id():
  event_id = "my-uuid-show2"
  events_repository = EventsRepository()
  response = events_repository.get_event_by_id(event_id)
  print(response)