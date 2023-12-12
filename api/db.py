from mariadb import Cursor, Connection, mariadb
from api.projectTypes import Animal, WeightSubmit


class Connection:
    cursor: Cursor
    connection: Connection

    user = "root"
    pw = "12345"  # bad practice, or even worst practice, but for this assignment its okay
    host = "127.0.0.1"
    port = 3306
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

    def get_amount_tracked_animals(self):
        sql = "SELECT JSON_OBJECT('amount', COUNT(*)) FROM animal;"

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_animals(self) -> list[str]:
        sql = "SELECT JSON_OBJECT('id', p_animal_id, 'name', name, 'species', species, 'sex', sex, 'weight', init_weight, 'birthday', birthday, 'created', created) FROM animal;"
        self.cursor.execute(sql)

        return self.cursor.fetchall()

    def get_animal(self, id: int) -> Animal:
        sql = "SELECT JSON_OBJECT('id', p_animal_id, 'name', name, 'species', species, 'sex', sex, 'weight', init_weight, 'birthday', birthday, 'created', created) FROM animal WHERE p_animal_id = %s;"

        self.cursor.execute(sql, (id,))

        return self.cursor.fetchall()

    def add_animal(self, data: Animal) -> bool:
        sql = "INSERT INTO animal (name, species, sex, init_weight, birthday) VALUES(%s, %s, %s, %s, %s);"

        self.cursor.execute(
            sql, (data.name, data.species, data.sex, data.weight, data.birthday)
        )
        self.connection.commit()

        return True

    def delete_animal(self, animal_id: int) -> bool:
        sql = "DELETE FROM animal WHERE p_animal_id = %s;"

        self.cursor.execute(sql, (animal_id,))
        self.connection.commit()

        return True

    def post_animal_weight(self, payload: WeightSubmit):
        sql = "INSERT INTO weight (f_animal_id, weight) VALUES (%s, %s);"

        self.cursor.execute(sql, (payload.id, payload.weight))
        self.connection.commit()

    def get_animal_weight(self, id):
        sql = "SELECT JSON_OBJECT('id', f_animal_id, 'weight', weight, 'created', created, 'weight_id', p_weight_id) FROM weight WHERE f_animal_id = %s"

        self.cursor.execute(sql, (id,))

        return self.cursor.fetchall()
