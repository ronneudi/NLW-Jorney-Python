from typing import Dict, List


class TripFinder:
    def __init__(self, trips_repository) -> None:
        self.__trips_repository = trips_repository

    def find_trip_details(self, trip_id) -> Dict:
        try:
            trip = self.__trips_repository.find_trip_by_id(trip_id)
            if not trip: raise Exception("No Trip Found")
            return {"body": {"trip": {"id": trip[0],"destination": trip[1], "start_at": trip[2],"ends_at": trip[3],"status": trip[6]}},"status_code": 200}
        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)}, "status_code": 400
            }

    def find_all_trips_detail(self) -> List[Dict]:
        try:
            trips = self.__trips_repository.find_all_trips()
            formatted_trips = []
            for trip in trips:
                formatted_trips.append({
                    "id": trip[0],
                    "destination": trip[1],
                    "start_at": trip[2],
                    "ends_at": trip[3],
                    "status": trip[6]
                })
            return {"body": {"trips": formatted_trips}, "status_code": 200}
        except Exception as exception:
            return {"body": {"error": "Bad Request", "message": str(exception)}, "status_code": 400}
