import pytest
from ..settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository
from uuid import uuid4

db_connection_handler.connect()
trip_id = str(uuid4())
link_id = str(uuid4())


def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repo = LinksRepository(conn)
    link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "google.com.br",
        "title": "Google"
    }
    link_repo.registry_link(link_infos)


def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    link_repo = LinksRepository(conn)
    result = link_repo.find_links_from_trip(trip_id)
    print(result)

