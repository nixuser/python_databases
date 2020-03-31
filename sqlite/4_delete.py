import sqlite3

connection = sqlite3.connect("data.sqlite")
cursor = connection.cursor()

# cursor.execute("DROP TABLE contacts_app;")
cursor.execute("DROP TABLE IF EXISTS contacts_app;")

# sql = "DELETE FROM contacts_app WHERE name = ?"
#
# cursor.execute(sql, ("HELLOTEST",))
# connection.commit()

connection.close()