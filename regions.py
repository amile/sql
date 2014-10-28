import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("create table regions (city text, region text)")
	cities = [
		('New York City', 'Northeast'),
		('San Francisco', 'West'),
		('Chicago', 'Midwest'),
		('Houston', 'South'),
		('Phoenix', 'West'),
		('Boston', 'Northeast'),
		('Los Angeles', 'West'),
		('Houston', 'South'),
		('Philadelphia', 'Northeast'),
		('San Antonio', 'South'),
		('Dallas', 'South'),
		('San Jose', 'West'),
		('Jacksonville', 'South'),
		('Indianapolis', 'Midwest'),
		('Austin', 'South'),
		('Detroit', 'Midwest')
	]
	c.executemany("insert into regions values(?, ?)", cities)
	c.execute("select * from regions order by region asc")
	regions = c.fetchall()
	for r in regions:
		print r[0], r[1]