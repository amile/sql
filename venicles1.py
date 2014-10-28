import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("update inventory set quantity = 2")

conn.commit()
cursor.execute("select * from inventory where make = 'Ford'")

fords = cursor.fetchall()

for ford in fords:
	print ford[0], ford[1], ford[2]

conn.close()