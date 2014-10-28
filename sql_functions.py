import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	queries = {
		'average': 'select avg(population) from population',
		'maximum': 'select max(population) from population',
		'minimum': 'select min(population) from population',
		'sum': 'select sum(population) from population',
		'count': 'select count(city) from population'
	}
	for keys, values in queries.iteritems():
		c.execute(values)
		val = c.fetchone()
		print keys + ': ' + str(val[0])