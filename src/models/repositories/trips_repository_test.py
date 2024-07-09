import pytest
from uuid import uuid4
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid4())


@pytest.mark.skip(reason="interação com banco")
def test_crete_base():
    conn = db_connection_handler.get_connection()
    cursor = conn.cursor()
    with open("init/schema.sql", "r") as file:
        script = file.read()
    cursor.executescript(script)


@pytest.mark.skip(reason="interação com banco")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)

    trips_infos = {
        "id": trip_id,
        "destination": "Osasco",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Osvaldo",
        "owner_email": "osvaldoresende@trips.com"
    }

    trips_repository.create_trip(trips_infos)


@pytest.mark.skip(reason="interação com banco")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    trip = trips_repository.find_trip_by_id(trip_id)
    print(trip)


@pytest.mark.skip(reason="interação com banco")
def test_update_trip_status_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    trips_repository.update_trip_status_by_id(trip_id)
