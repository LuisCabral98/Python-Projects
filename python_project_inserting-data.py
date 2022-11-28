import mysql.connector

user_input = input("To input data into the table, press 1. \n")

while user_input == '1':
	db = mysql.connector.connect(host='localhost', user='root', password='3282Hull!', database='independent_project_employeeData', auth_plugin='mysql_native_password')

	cur = db.cursor()

	user_ID = input("What is the employee ID?")

	user_firstName = input("What is the employee's first name?")

	user_lastName = input("What is the employee's last name?")

	user_email = input("What is the employee's email?")

	cur.execute("INSERT INTO employeeData (ID, firstName, lastName, email) VALUES ('{}', '{}', '{}', '{}')".format(user_ID, user_firstName,	user_lastName, user_email))

	db.commit()

	print(cur.rowcount, "was inserted.")

	user_input = input("Would you like to insert more? If so, press 1. \n")

	if user_input == '1':
		continue
	else:
		break