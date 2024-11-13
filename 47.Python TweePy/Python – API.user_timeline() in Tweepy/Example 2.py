# screen name of the account to be fetched
from requests import api

screen_name = "geeksforgeeks"

# number of statuses to be fetched
count = 3

# fetching the statuses
statuses = api.user_timeline(screen_name, count = count)

# printing the statuses
for status in statuses:
	print(status.text, end = "\n\n")
