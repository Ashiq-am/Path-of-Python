# the screen name of the user
import location as location

screen_name = "PracticeGfG"

# fetching the user
user = api.get_user(screen_name)

# fetching the name
name = user.name

if location == "":
	print("The user has not mentioned their loaction.")
else:
	print("The location of the user is : " + location)
