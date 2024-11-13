# list of screen_names
screen_names = ["geeksforgeeks", "PracticeGfG", "GeeksQuiz"]

# getting the users by screen_names
users = api.lookup_users(screen_names = screen_names)

# printing the user details
for user in users:
	print("The id is : " + str(user.id))
	print("The screen name is : " + user.screen_name, end = "\n\n")
