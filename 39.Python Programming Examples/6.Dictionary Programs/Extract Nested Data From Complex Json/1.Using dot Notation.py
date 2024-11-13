# Extract nested data using dot notation
country_dot = data["location"]["country"]
city_dot = data["location"]["city"]

print(f"Extracted Data using Dot Notation:")
print(f"Country: {country_dot}")
print(f"City: {city_dot}")
