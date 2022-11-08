import sqlite3 as sql

from cereal import Cereal


class DbTool:
    def __init__(self) -> None:
        from constants import DATABASE, RESET_DATABASE
        self.conn = DATABASE


    def get_cereals(self) -> list[Cereal]:
        with sql.connect(self.conn) as conn:
            conn.row_factory = sql.Row
            c = conn.cursor()
            c.execute("SELECT * FROM Cereal")

            return [Cereal(dict(x)) for x in c.fetchall()]

    def get_cereal(self, id: int) -> Cereal:
        with sql.connect(self.conn) as conn:
            conn.row_factory = sql.Row
            c = conn.cursor()
            c.execute(f"SELECT * FROM Cereal WHERE Id = {id}")
            return Cereal(dict(c.fetchone()))

    def reset_database(self):
        from parsers import csv_parser
        cereal_box = csv_parser.read_cereal()

        with sql.connect(self.conn) as conn:
            cursor = conn.cursor()
            cursor.executescript(self.CREATE_TABLE)
            cursor.executemany(self.INSERT_INTO, [cereal.get_values for cereal in cereal_box])

    @property
    def CREATE_TABLE(self) -> str:
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
    def INSERT_INTO(self) -> str:
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

