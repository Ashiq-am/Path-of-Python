# Create a list of nested JSON objects
data = [{"id": "123",
		"author":
		{
			"firstname": "Jane",
			"lastname": "Doe"
		},
		"editor":
		{
			"firstname": "Jane",
			"lastname": "Smith"
		},
		"title": "The Ultimate Database Study Guide",
		"category": ["Non-Fiction", "Technology"]
		},
		{"id": "120",
		"author":
		{
			"lastname": "Gunjan",
			"firstname": "Pawan"
		},
		"editor":
		{
			"lastname": "Gunjan",
			"firstname": "Nitya"
		},
		"title": "Om",
		"category": ["Spritual", "Meditations"]
		}
		]

# Normalize the list of JSON objects into a Pandas dataframe
df = pd.json_normalize(data)
print(df)
