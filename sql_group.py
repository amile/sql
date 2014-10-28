import sqlite3

with sqlite3.connect("cars.db") as connection:
	c = connection.cursor()
	c.execute("""select orders.make, orders.model, 
		inventory.quantity, count(orders.model)
		from inventory, orders
		where 
		inventory.make = orders.make and
		inventory.model = orders.model
		group by orders.model""")
	result = c.fetchall()
	for r in result:
		print r[0], r[1]
		print "Total quantity:", r[2]
		print "Number of orders: ", r[3], "\n"