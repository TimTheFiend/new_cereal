def parse_query(query: str) -> str:
    return " AND ".join(query.split(';'))

def parse_advanced_query(query: dict[str, str]):
    """Iterates through dictionary and returns a str containing the SQL statement for `WHERE`
    """
    operator = ""
    conditionals = []

    for index, values in enumerate(query.items()):
        """The order of the dictionary goes:
        0: x_operator
        1: x
        2: y_operator
        3: y
        etc.
        """
        key = values[0]
        value = values[1]
        if index % 2 == 0:
            operator = value
        else:
            if value != "":
                conditionals.append(f"{key}{operator}{value}")
                continue
            operator = ""
    return " AND ".join(x for x in conditionals)
