import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New register in database")
def test_insert_attendee():
  event_id = "my-uuid-show"
  attendees_info = {
    "uuid": "my_uuid_attendee",
    "name": "John Doe",
    "email": "johndoe@example.com",
    "event_id": event_id,
  }
  attendees_repository = AttendeesRepository()
  response = attendees_repository.insert_attendee(attendees_info)
  print(response)

def test_get_attendee_badge_by_id():
  attendee_id = "my_uuid_attendee"
  attendees_repository = AttendeesRepository()
  attendee = attendees_repository.get_attendee_badge_by_id(attendee_id)

  print(attendee)
  print(attendee.title)