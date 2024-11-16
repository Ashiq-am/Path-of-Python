import pandas as pd

data = [
	{
		"id": 1,
		"candidate": "Roberto mathews",
		"health_index": {"bmi": 22, "blood_pressure": 130},
	},
	{"candidate": "Shane wade", "health_index": {"bmi": 28, "blood_pressure": 160}},
	{
		"id": 2,
		"candidate": "Bruce tommy",
		"health_index": {"bmi": 31, "blood_pressure": 190},
	},
]
pd.json_normalize(data, max_level=1)
