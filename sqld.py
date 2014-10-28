import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

try:
	cursor.execute("insert into populations values\
		('New York City', 'NY', 8200000)")
	cursor.execute("insert into populations values\
		('San Francisco', 'CA', 800000)")
except sqlite3.OperationalError as e:
	print "Oops! Something went wrong. Try again...", e

conn.close()