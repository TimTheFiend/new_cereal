import csv

from cereal import Cereal
from constants import CEREAL_CSV

def read_cereal():
    with open(CEREAL_CSV) as file:
    # with open(r"files\cereal.csv") as file:
        reader = csv.DictReader(file, delimiter=';')
        d = {row_index : row for row_index, row in enumerate(reader)}
        d.pop(0)
        cereal_box = [Cereal(v) for k, v in d.items()]
        return cereal_box