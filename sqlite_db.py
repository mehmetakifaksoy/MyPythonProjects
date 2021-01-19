import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("select * from employees")
result = cursor.fetchall()
print(result)

connection.close()