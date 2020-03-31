from postgres_example.config import connection, cursor, config

# Выполняем запрос
cursor.execute(f"UPDATE {config.TABLE} SET name = %s WHERE name = %s", ("TEST", "Vasya"))
connection.commit()

# Изменяем таблицу
cursor.execute(f"ALTER TABLE {config.TABLE} DROP address")
connection.commit()

# Закрываемся
cursor.close()
connection.close()
