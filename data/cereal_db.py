import sqlite3 as sql

from cereal import Cereal


class DbTool:
    def __init__(self) -> None:
        from constants import DATABASE, RESET_DATABASE
        self.conn = DATABASE

        if RESET_DATABASE:
            self.reset_database()


    """GET ALL"""
    def get_cereals(self) -> list[Cereal]:
        with sql.connect(self.conn) as conn:
            conn.row_factory = sql.Row
            c = conn.cursor()
            c.execute("SELECT * FROM Cereal")

            return [Cereal(dict(x)) for x in c.fetchall()]


    """GET ONE"""
    def get_cereal(self, id: int) -> Cereal:
        try:
            with sql.connect(self.conn) as conn:
                conn.row_factory = sql.Row
                c = conn.cursor()
                c.execute(f"SELECT * FROM Cereal WHERE Id = {id}")
                return Cereal(dict(c.fetchone()))
        except:
            return None

    """GET SELECTED"""
    def get_query_cereals(self, query : str, orderby: str = "") -> list[Cereal]:
        try:
            with sql.connect(self.conn) as conn:
                conn.row_factory = sql.Row
                c = conn.cursor()
                _sql = f'SELECT * FROM Cereal WHERE {query} '
                if orderby != "":
                    _sql += f" ORDER BY {orderby}"
                c.execute(_sql)
                return [Cereal(dict(x)) for x in c.fetchall()]
        except:
            return None

    def on_update(self, request: dict):
        if (cereal_id := request['id']) == "":
            self.add_cereal(Cereal(request))
            return True
        elif self.get_cereal(int(cereal_id)) != None:
            self.update_cereal(cereal_id, Cereal(request))
            return True
        return False


    """UPDATE"""
    def update_cereal(self, id_to_update: int, new_cereal: Cereal) -> bool:
        if (old_cereal := self.get_cereal(id=id_to_update)) is None:
            return False

        new_cereal.id = old_cereal.id

        with sql.connect(self.conn) as conn:
            conn.row_factory = sql.Row
            c = conn.cursor()
            c.execute(self.UPDATE_WHERE_CEREAL, new_cereal.get_values_for_update)
            conn.commit()
            return True


    def add_cereal(self, cereal: Cereal) -> int:
        try:
            with sql.connect(self.conn) as conn:
                conn.row_factory = sql.Row
                c = conn.cursor()
                c.execute(self.INSERT_INTO_CEREAL, cereal.get_values)
                conn.commit()
                return True
        except:
            return False

    def delete_cereal(self, id: int) -> bool:
        try:
            with sql.connect(self.conn) as conn:
                c = conn.cursor()
                c.execute(f"DELETE FROM Cereal WHERE ID = {id}")
                conn.commit()
                return True
        except:
            return False


    def reset_database(self):
        from parsers import csv_parser
        cereal_box = csv_parser.read_cereal()

        with sql.connect(self.conn) as conn:
            c = conn.cursor()
            # CEREAL TABLE
            c.executescript(self.CREATE_CEREAL_TABLE)
            c.executemany(self.INSERT_INTO_CEREAL, [cereal.get_values for cereal in cereal_box])
            # USER TABLE
            c.executescript(self.CREATE_TABLE_USER)
            c.execute(self.INSERT_INTO_USER)

    def attempt_login(self, username: str, password: str) -> bool:
        try:
            with sql.connect(self.conn) as conn:
                c = conn.cursor()
                c.execute(f"SELECT * FROM User WHERE Username = \"{username}\" AND Password = \"{password}\"")
                user = c.fetchone()
                if user is not None:
                    return True
                return False
        except:
            return False

    @property
    def CREATE_TABLE_USER(self) -> str:
        return """
            DROP TABLE IF EXISTS User;
            CREATE TABLE User(
                Id INTEGER PRIMARY KEY,
                Username TEXT,
                Password TEXT
            );
            """

    @property
    def INSERT_INTO_USER(self) -> str:
        return """
            INSERT INTO User(Username, Password)
            VALUES (
                "admin",
                "root"
            )
        """

    @property
    def CREATE_CEREAL_TABLE(self) -> str:
        return """
            DROP TABLE IF EXISTS Cereal;
            CREATE TABLE Cereal(
                Id INTEGER PRIMARY KEY,
                Name TEXT,
                MFR TEXT,
                Type TEXT,
                Calories INT,
                Protein INT,
                Fat INT,
                Sodium INT,
                Fiber REAL,
                Carbo REAL,
                Sugars INT,
                Potass INT,
                Vitamins INT,
                Shelf INT,
                Weight REAL,
                Cups REAL,
                Rating TEXT,
                Image TEXT
            );
            """


    @property
    def INSERT_INTO_CEREAL(self) -> str:
        return """
            INSERT INTO Cereal(
                Name,
                MFR,
                Type,
                Calories,
                Protein,
                Fat,
                Sodium,
                Fiber,
                Carbo,
                Sugars,
                Potass,
                Vitamins,
                Shelf,
                Weight,
                Cups,
                Rating
            )
            VALUES(
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?,
                ?
            )
            """

    @property
    def UPDATE_WHERE_CEREAL(self) -> str:
        return """
            UPDATE Cereal SET
                Name = ?,
                MFR = ?,
                Type = ?,
                Calories = ?,
                Protein = ?,
                Fat = ?,
                Sodium = ?,
                Fiber = ?,
                Carbo = ?,
                Sugars = ?,
                Potass = ?,
                Vitamins = ?,
                Shelf = ?,
                Weight = ?,
                Cups = ?,
                Rating = ?
            WHERE Id = ?;
            """