from typing import Dict
from uuid import uuid4


class LinkCreator:
    def __init__(self, links_repository) -> None:
        self.__links_repository = links_repository

    def creator(self, body, trip_id) -> Dict:
        try:
            link_id = str(uuid4())
            link_infos = {**body, "id": link_id, "trip_id": trip_id}
            self.__links_repository.registry_link(link_infos)
            return {"body": {"linkId": link_id}, "status_code": 201}
        except Exception as exception:
            return {"body": {"error": "Bad Request", "message": str(exception)}, "status_code": 400}
