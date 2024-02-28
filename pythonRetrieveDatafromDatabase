import mysql.connector

user_choice = input("Welcome to the employee database! To continue press 1.")

while user_choice == '1':

	user_choice = True

	db = mysql.connector.connect(host='localhost', user='root', password='3282Hull!', database='independent_project_employeeData', auth_plugin='mysql_native_password')

	cur = db.cursor()

	user_input = input("Please enter an employee ID to retrieve info about them: ")

	cur.execute("""SELECT * FROM employeeData WHERE ID LIKE ('%s')""" % user_input)

	data = cur.fetchall()

	for row in data:
		print (row)

	user_choice = input("Would you like to continue? Press 1 if so. If not, enter any other key.")

	if user_choice == '1':
		continue
	else:
		break	