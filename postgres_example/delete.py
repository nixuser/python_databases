from postgres_example.config import connection, cursor

TABLE = "contacts"

# Execute delete data query
cursor.execute(f"DELETE FROM {TABLE} WHERE name='Test'")
connection.commit()

# CLosing connections
cursor.close()
connection.close()