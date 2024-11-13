# the screen name of the user
screen_name = "PracticeGfG"

# fetching the user
user = api.get_user(screen_name)

# fetching the favourites_count attribute
favourites_count = user.favourites_count

print("The number of tweets the user has liked are : " + str(favourites_count))
