response_json = response.json()
print(f"keys in the Json file : {response_json.keys()}")
print(f"Total javascript repositories in GitHub : {response_json['total_count']}" )
