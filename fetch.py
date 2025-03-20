def execute_query(connection, query, params=()):
    """Executes a query without fetching data."""
    cursor = connection.cursor_connection
    cursor.execute(query, params)
    connection.database_connection.commit()


def fetch_one(connection, query, params=()):
    """Fetches a single row from the database."""
    cursor = connection.cursor_connection
    cursor.execute(query, params)
    return cursor.fetchone()


def fetch_all(connection, query, params=()):
    """Fetches all rows from the database."""
    cursor = connection.cursor_connection
    cursor.execute(query, params)
    return cursor.fetchall()
