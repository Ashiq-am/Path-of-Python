# Creating dictionary which contains lists
country = {
	"India": ["Delhi", "Maharastra", "Haryana",
			"Uttar Pradesh", "Himachal Pradesh"],
	"Japan": ["Hokkaido", "Chubu", "Tohoku", "Shikoku"],
	"United States": ["New York", "Texas", "Indiana",
					"New Jersey", "Hawaii", "Alaska"]
}

for key, val in country.items():
	for i in val:
		print("{} : {}".format(key, i))
	print("--------------------")
