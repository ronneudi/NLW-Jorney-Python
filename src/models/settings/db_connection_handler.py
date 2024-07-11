from sqlite3 import connect, Connection


class DbConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "storage.db"
        self.__conn = None

    def connect(self) -> None:
        conn = connect(self.__connection_string, check_same_thread=False)
        self.__conn = conn

    def get_connection(self) -> Connection:
        return self.__conn

    def create(self) -> None:
        conn = self.get_connection()
        cursor = conn.cursor()
        with open("init/schema.sql", "r") as file:
            script = file.read()
        cursor.executescript(script)
        conn.commit()


db_connection_handler = DbConnectionHandler()
