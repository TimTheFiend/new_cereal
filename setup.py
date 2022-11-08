from constants import RESET_DATABASE
from data import cereal_db
from parsers import csv_parser

from cereal import Cereal


db = cereal_db.DbTool()


if __name__ == "__main__":
    if RESET_DATABASE:
        db.reset_database()
    # cereal_box = db.get_all_dict()
    cereal_box = db.get_cereal(1)
    # cereal_box = [Cereal(dict(x)) for x in db.get_all_dict()]

    print(cereal_box.name)