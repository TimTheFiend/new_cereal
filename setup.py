from constants import RESET_DATABASE
from data import cereal_db
from parsers.query_parser import parse_query
from cereal import Cereal


db = cereal_db.DbTool()


QUERY = "calories>=100;id<10"
GET_ID = 1
UPDATED_ID = 2

CEREAL_DICT = {
    "name" : "Tricky Dicky O's",
    "mfr" : "A",
    "type" : "S",
    "calories" : "123",
    "protein" : "312",
    "fat" : "123",
    "sodium" : "312",
    "fiber" : "15432",
    "carbo" : "123123",
    "sugars" : "124123",
    "potass" : "142214",
    "vitamins" : "123213",
    "shelf" : "321312",
    "weight" : "312",
    "cups" : "412",
    "rating" : "123",
}


if __name__ == "__main__":
    if RESET_DATABASE:
        db.reset_database()


    """TEST GET ALL"""
    all_cereal = db.get_cereals()
    assert len(all_cereal) == 77
    """TEST GET SINGLE"""
    single_cereal = db.get_cereal(GET_ID)
    assert single_cereal.id == GET_ID
    """TEST GET SELECTED"""
    select_cereals = db.get_query_cereals(parse_query(QUERY))
    assert len(select_cereals) == 5
    """TEST UPDATE"""
    single_cereal.id = UPDATED_ID
    assert db.update_cereal(UPDATED_ID, single_cereal) is True
    ## Extra test
    updated_cereal = db.get_cereal(2)
    assert single_cereal.name == updated_cereal.name
    """POST ADD"""
    assert db.add_cereal(cereal=Cereal(CEREAL_DICT)) == True
    all_cereal = db.get_cereals()
    print()