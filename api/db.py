from mariadb import Cursor, Connection, mariadb


class Connection:
    cursor: Cursor
    connection: Connection

    user = "root"
    pw = 12345 # bad practice, or even worst practice, but for this assignment its okay
    host: str = "127.0.0.1"
    port: str = "3306"
    database = "weight_tracker"

    def __init__(self) -> None:
        self.connect_to_db()

    def connect_to_db(self):
        try:
            conn = mariadb.connect(
                user=self.user,
                password=self.pw,
                host=self.host,
                port=self.port,
                database=self.database,
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            exit(1)

        self.connection = conn
        self.cursor = conn.cursor()

    def get_animals(self) -> list[str]:
        sql = "SELECT * FROM animal"
        self.cursor.execute(sql)

        return self.cursor.fetchall()
