import sqlite3

with sqlite3.connect("new.db") as conn:

	cursor = conn.cursor()

	cursor.execute("""select population.city, population.population,
		regions.region from population, regions
		where population.city = regions.city""")

	rows = cursor.fetchall()
	for r in rows:
		print r[0], r[1], r[2]

