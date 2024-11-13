# fetching the trends
trends = api.trends_available()

print("Some of the locations are : ")
for i in range(0, 200, 20):
	print("Place : " + trends[i]['name'] +
		", Country : " + trends[i]['country'])
