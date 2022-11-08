from constants import RESET_DATABASE
from data import cereal_db
from parsers import csv_parser

from cereal import Cereal


db = cereal_db.DbTool()


if __name__ == "__main__":
    if RESET_DATABASE:
        db.reset_database()
