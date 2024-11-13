# WOEID of New York
woeid = 2459115

# fetching the trends
trends = api.trends_place(id = woeid, exclude = "hashtags")

# printing the information
print("The top trends for the location are :")

for value in trends:
	for trend in value['trends']:
		print(trend['name'])
