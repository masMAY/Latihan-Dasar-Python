print "Nested Conditional"

username = raw_input("Input Username :")
password = raw_input("Input password :")

username_from_db = "user"
password_from_db = "admin"

if username == username_from_db:
	if password == password_from_db:
		print "Username and Pasword are correct"
	else:
		print "Password is uncorrect"
else:
	print "User Undefined"
