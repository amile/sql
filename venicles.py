import sqlite3
import csv

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

venicles = csv.reader(open("venicles.csv", "rU"))

cursor.executemany("insert into inventory values(?, ?, ?)", venicles)

conn.commit()

cursor.execute("select * from inventory")

rows = cursor.fetchall()

for r in rows:
	print r[0], r[1], r[2]

conn.close()