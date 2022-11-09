def parse_query(query: str) -> str:
    return " AND ".join(query.split(';'))