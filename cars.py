import sqlite3

conn = sqlite3.connect("cars.db")

cursor = conn.cursor()

cursor.execute("""create table inventory 
				(make text, model text, quantity int)
				""") 

conn.close()