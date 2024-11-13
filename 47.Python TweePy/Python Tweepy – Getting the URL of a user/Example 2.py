# the screen name of the user
screen_name = "PracticeGfG"

# fetching the user
user = api.get_user(screen_name)

# fetching the url
url = user.url

print("The URL of the user is : " + url)
