Details = {"Destination": "China",
		"Nationality": "Italian", "Age": [20]}
print("Original:", Details)

if "Age" in Details:
	Details["Age"].append("Twenty")
	print("Modified:", Details)
