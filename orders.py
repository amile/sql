import sqlite3
import csv

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	orders = csv.reader(open("orders.csv", "rU"))
	c.execute("create table orders \
		(make text, model text, order_date date)")
	c.executemany("insert into orders values(?, ?, ?)", orders)
	c.execute("""select distinct inventory.make, inventory.model, 
		inventory.quantity, orders.order_date
		from inventory, orders
		where 
		inventory.make = orders.make and
		inventory.model = orders.model
		order by inventory.make asc
		""")
	cars = c.fetchall()
	for c in cars:
		print c[0], c[1]
		print "quantity: " + str(c[2])
		print "      order_date: " + str(c[3])
		print "__________________"


