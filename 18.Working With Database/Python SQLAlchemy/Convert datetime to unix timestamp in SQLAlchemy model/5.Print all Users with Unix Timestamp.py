# query the database
users = session.query(User).all()

# print the users
for user in users:
	print(user)
