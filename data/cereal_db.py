import sqlite3 as sql

from cereal import Cereal


class DbTool:
    def __init__(self) -> None:
        from constants import DATABASE, RESET_DATABASE
        self.conn = DATABASE


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
    def get_query_cereals(self, query : str) -> list[Cereal]:
        with sql.connect(self.conn) as conn:
            conn.row_factory = sql.Row
            c = conn.cursor()
            c.execute(f'SELECT * FROM Cereal WHERE {query}')
            return [Cereal(dict(x)) for x in c.fetchall()]


    """UPDATE"""
    def update_cereal(self, id_to_update: int, new_cereal: Cereal) -> bool:
        if (old_cereal := self.get_cereal(id=id_to_update)) is None:
            return False

        new_cereal.id = old_cereal.id

        with sql.connect(self.conn) as conn:
            conn.row_factory = sql.Row
            c = conn.cursor()
            c.execute(self.UPDATE_WHERE, new_cereal.get_values_for_update)
            return True

    def add_cereal(self, cereal: Cereal) -> int:
        try:
            with sql.connect(self.conn) as conn:
                conn.row_factory = sql.Row
                c = conn.cursor()
                c.execute(self.INSERT_INTO, cereal.get_values)
                conn.commit()
                return True
        except:
            return False


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

    @property
    def UPDATE_WHERE(self) -> str:
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