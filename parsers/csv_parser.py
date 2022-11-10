import csv

from cereal import Cereal
from constants import CEREAL_CSV

def read_cereal():
    """Reads `CEREAL_CSV`-file, and returns the content as a `list[Cereal]`-object.
    Pops the 0th element in the CSV, since it's the typing for the header.
    """
    with open(CEREAL_CSV) as file:
        reader = csv.DictReader(file, delimiter=';')
        d = {row_index : row for row_index, row in enumerate(reader)}
        d.pop(0)
        cereal_box = [Cereal(v) for k, v in d.items()]
        return cereal_box