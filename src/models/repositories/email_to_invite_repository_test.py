import pytest
from uuid import uuid4
from datetime import datetime, timedelta
from .email_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid4())
email_id = str(uuid4())


@pytest.mark.skip(reason="interação com banco")
def test_regitry_email():
    conn = db_connection_handler.get_connection()
    email_repository = EmailsToInviteRepository(conn)

    email_infos = {
        "id": email_id,
        "trip_id": trip_id,
        "email": "mymail@contoso.com"
    }

    email_repository.registry_email(email_infos)


@pytest.mark.skip(reason="interação com banco")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    email_repository = EmailsToInviteRepository(conn)
    mail = email_repository.find_email_from_trip(trip_id)
    print(mail)
