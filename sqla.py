import sqlite3

# create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

#create a table

cursor.execute("""create table population
				(city text, state text, population int)
				""")
# close the database connection
conn.close()