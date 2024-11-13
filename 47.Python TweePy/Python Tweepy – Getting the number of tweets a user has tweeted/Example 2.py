# the screen name of the user
screen_name = "PracticeGfG"

# fetching the user
user = api.get_user(screen_name)

# fetching the statuses_count attribute
statuses_count = user.statuses_count

print("The number of statuses the user has posted are : " + str(statuses_count))
