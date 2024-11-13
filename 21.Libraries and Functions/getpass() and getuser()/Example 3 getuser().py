# Python program to demonstrate working of
# getpass.getuser()
import getpass

user = getpass.getuser()

while True:
	pwd = getpass.getpass("User Name : %s" % user)

	if pwd == 'Adiba':
		print("Welcome!!!")
		break
	else:
		print("The password you entered is incorrect.")
