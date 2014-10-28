import sqlite3
import random

def insert_random_numbers(db, n):
	val = [(random.randint(0, n),) for i in xrange(n)]
	#val.sort()
	with sqlite3.connect(db) as connection:
		c = connection.cursor()
		c.execute("drop table if exists integers")
		c.execute("create table integers(number int)")
		c.executemany("insert into integers values(?)", val)

def insert_random_numbers2(db, n):
	with sqlite3.connect(db) as connection:
		c = connection.cursor()
		# delete database table if exist
		c.execute("DROP TABLE if exists numbers")

		# create database table
		c.execute("CREATE TABLE numbers(num int)")
		# insert each number to the database
		for i in xrange(n):
			c.execute("INSERT INTO numbers VALUES(?)",
				(random.randint(0,n),))

if __name__ == '__main__':
	import timeit
	print(timeit.timeit('insert_random_numbers(":memory:", 1000)',
		setup="from __main__ import insert_random_numbers",
		number=100,
	))
	print(timeit.timeit('insert_random_numbers2(":memory:", 1000)',
		setup="from __main__ import insert_random_numbers2",
		number=100,
	))
