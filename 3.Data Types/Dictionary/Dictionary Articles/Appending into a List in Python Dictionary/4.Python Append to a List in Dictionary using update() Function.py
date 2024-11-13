Details = {"Destination": "China",
		"Nationality": "Italian"}
Details["Age"] = []
print("Original:", Details)

# using update() function
Details.update({"Age": [18, 20, 25, 29, 30]})
print("Modified:", Details)
