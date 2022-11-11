def parse_query(query: str) -> str:
    return " AND ".join(query.split(';'))

def parse_advanced_query(query: dict[str, str]):
    """Iterates through dictionary and returns a str containing the SQL statement for `WHERE`
    """
    operator = ""
    conditionals = []

    if query.get('mfr') or query.get('type'):
        print()

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
                if key not in ['mfr', 'type']:
                    conditionals.append(f"{key}{operator}{value}")
                    continue
                conditionals.append(f'{key}="{value.upper()}"')
                continue
            operator = ""
    return " AND ".join(x for x in conditionals)
