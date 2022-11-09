def parse_query(query: str) -> str:
    return " AND ".join(query.split(';'))

def parse_advanced_query(query: dict[str, str]):
    operator = ""
    conditionals = []

    for index, values in enumerate(query.items()):
        key = values[0]
        value = values[1]
        if index % 2 == 0:
            operator = value
        else:
            if value != "":
                conditionals.append(f"{key}{operator}{value}")
                continue
            operator = ""
    result = " AND ".join(conditionals)
    return " AND ".join(x for x in conditionals)
