import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("insert into population values('New Yort City', \
	'NY', 8200000)")
	c.execute("insert into population values('San Francisco', \
	'CA', 800000)")
