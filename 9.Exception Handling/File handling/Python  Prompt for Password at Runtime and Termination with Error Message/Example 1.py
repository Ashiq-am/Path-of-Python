import getpass
user = getpass.getuser()
passwd = getpass.getpass()

# must write svc_login()
if svc_login(user, passwd):
	print('Yay !')
else:
	print('Boo !')
