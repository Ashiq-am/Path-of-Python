# number of statuses to be fetched
count = 5

# fetching the statuses
statuses = api.home_timeline(count = count)

# printing the screen names of each status
for status in statuses:
	print(status.user.screen_name)
