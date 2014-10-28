import sqlite3

with sqlite3.connect("newnum.db") as connection:
	c = connection.cursor()
	
	perform = {
		1: 'avg', 2: 'max', 3: 'min', 
		4:'sum', 5:'exit'
	}
	while True:
		ans = raw_input("""
		Select the operation what you whant to perform [1-5]:
		1 - average
		2 - maximum
		3 - minimum
		4 - sum
		5 - exit
		""")
		if ans.isdigit() == False or int(ans) not in perform:
			print "Your input is incorrect"
			continue
		ans = int(ans)
		if ans in perform and ans != 5:
			c.execute('select {}(number) from integers'.format(perform[ans]))
			result = c.fetchone()
			print perform[ans] + ':', str(result[0])
		elif ans == 5:
			print "Exit"
			break