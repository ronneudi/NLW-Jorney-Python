from datetime import datetime, timedelta

import pytest

from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.email_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler
from faker import Faker

faker = Faker()
db_connection_handler.connect()
db_connection_handler.create()
trip_id = str(faker.uuid4())
destination = faker.city()
owner_name = faker.name_nonbinary()
owner_mail = faker.email()
date_ini = faker.future_datetime()
start_at = date_ini.strftime("%d-%m-%Y")
end_at = faker.date_time_between(start_date=date_ini, end_date="+180d").strftime("%d-%m-%Y")
link_id = str(faker.uuid4())
link_url = faker.url()
link_title = faker.domain_word()
email_id = str(faker.uuid4())
email_mail = faker.email()
prt_id = str(faker.uuid4())


@pytest.mark.skip
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepository(conn)
    trips_infos = {
        "id": trip_id,
        "destination": destination,
        "start_date": start_at,
        "end_date": end_at,
        "owner_name": owner_name,
        "owner_email": owner_mail
    }
    trips_repo.create_trip(trips_infos)


@pytest.mark.skip
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepository(conn)
    trip = trips_repo.find_trip_by_id(trip_id)
    print(trip)
    assert trip[0] == trip_id
    assert trip[1] == destination
    assert trip[2] == start_at
    assert trip[3] == end_at
    assert trip[4] == owner_name
    assert trip[5] == owner_mail


@pytest.mark.skip
def test_update_trip_status_by_id():
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepository(conn)
    trips_repo.update_trip_status_by_id(trip_id)
    trip = trips_repo.find_trip_by_id(trip_id)

    assert trip[6] == 1


@pytest.mark.skip
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repo = LinksRepository(conn)
    link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": link_url,
        "title": link_title
    }
    link_repo.registry_link(link_infos)


@pytest.mark.skip
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_repo = LinksRepository(conn)
    links = link_repo.find_links_from_trip(trip_id)

    assert links[0][0] == link_id


@pytest.mark.skip
def test_registry_activity():
    conn = db_connection_handler.get_connection()
    act_repo = ActivitiesRepository(conn)
    act_infos = {
        "id": str(faker.uuid4()),
        "trip_id": trip_id,
        "title": faker.city(),
        "occurs_at": faker.future_date().strftime("%d-%m-%Y")
    }
    act_repo.regitry_activity(act_infos)


@pytest.mark.skip
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    act_repo = ActivitiesRepository(conn)
    acts = act_repo.find_activities_from_trip(trip_id)

    assert acts[0][1] == trip_id


@pytest.mark.skip
def test_regitry_email():
    conn = db_connection_handler.get_connection()
    email_repository = EmailsToInviteRepository(conn)

    email_infos = {
        "id": email_id,
        "trip_id": trip_id,
        "email": email_mail
    }

    email_repository.registry_email(email_infos)


@pytest.mark.skip
def test_find_email_from_trip():
    conn = db_connection_handler.get_connection()
    email_repository = EmailsToInviteRepository(conn)
    mail = email_repository.find_email_from_trip(trip_id)
    assert mail[0][0] == email_id


@pytest.mark.skip
def test_registry_participats():
    conn = db_connection_handler.get_connection()
    prt_repo = ParticipantsRepository(conn)
    prt_infos = {
        "id": prt_id,
        "trip_id": trip_id,
        "emails_to_invite_id": email_id,
        "name": faker.name()
    }
    prt_repo.registry_participant(prt_infos)


@pytest.mark.skip
def test_find_participants_from_trip():
    conn = db_connection_handler.get_connection()
    prt_repo = ParticipantsRepository(conn)
    prts = prt_repo.find_participants_from_trip(trip_id)
    assert (prts == [] or prts[0][0] == trip_id)


@pytest.mark.skip
def test_update_participants_status():
    conn = db_connection_handler.get_connection()
    prt_repo = ParticipantsRepository(conn)
    prt_repo.update_participant_status(trip_id, prt_id)
