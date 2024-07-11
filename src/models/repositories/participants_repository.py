from sqlite3 import Connection
from typing import Dict, List, Tuple


class ParticipantsRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_participant(self, participant_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute("""
            INSERT INTO
            (id, trip_id, emails_to_invite_id, name)
            VALUES
            (?, ?, ?, ?)
        """), (
            participant_infos["id"],
            participant_infos["trip_id"],
            participant_infos["emails_to_invite_id"],
            participant_infos["name"]
        )
        self.__conn.commit()

    def find_participants_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute("""
            SELECT 1 FROM participants as a
            INNER JOIN emails_to_invite as b on b.id = a.emails_to_invite_id
            WHERE a.trip_id = ?
        """), (trip_id,)
        participants = cursor.fetchall()
        return participants

    def update_participant_status(self, trip_id: str, participant_id: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute("UPDATE participants SET is_confirmed = 1 WHERE id = ? AND trip_id = ?", (participant_id, trip_id))
        self.__conn.commit()
