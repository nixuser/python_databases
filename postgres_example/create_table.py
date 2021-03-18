import psycopg2
from postgres_example.config import connection, cursor

SQL = """
CREATE TABLE contacts (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    email TEXT,
    phone TEXT NOT NULL,
    address TEXT
);
"""

try:
    with open(SQL.strip(), "r") as script:
        cursor.execute(script.read())
except psycopg2.errors.DuplicateTable as e:
    print(e)

cursor.close()
connection.close()
