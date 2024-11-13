# Creating dictionary which contains lists
country = {
	"India": ["Delhi", "Maharastra", "Haryana",
			"Uttar Pradesh", "Himachal Pradesh"],
	"Japan": ["Hokkaido", "Chubu", "Tohoku", "Shikoku"],
	"United States": ["New York", "Texas", "Indiana",
					"New Jersey", "Hawaii", "Alaska"]
}

# extract the first 3 cities of India
print(country["India"][:3])

# extract last 2 cities from Japan
print(country["Japan"][-2:])

# extract all cities except last 3 cities from india
print(country["India"][:-3])

# extract 2th to 5th cities from us
print(country["United States"][1:5])
