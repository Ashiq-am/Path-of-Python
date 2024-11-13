import requests
import json

api_url = "http://localhost:8000/Hello-world"

response = requests.get(api_url)

if response.status_code == 200:
	new_data = response.json()

	try:
		with open("data.json", "r") as json_file:
			existing_data = json.load(json_file)
	except (FileNotFoundError, json.decoder.JSONDecodeError):
		existing_data = []

	existing_data.append(new_data)

	with open("data.json", "w") as json_file:
		json.dump(existing_data, json_file, indent=4)
		print("Data appended to data.json file.")
else:
	print("Failed to retrieve data from the API. Status code:", response.status_code)
