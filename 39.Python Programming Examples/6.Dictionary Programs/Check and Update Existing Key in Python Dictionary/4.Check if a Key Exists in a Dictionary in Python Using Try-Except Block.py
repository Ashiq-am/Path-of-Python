# Initial dictionary
user = {'name': 'Geek', 'rank': 10, 'city': 'Geek Town'}

# Update existing key using try-except block
try:
	user['age'] = user.pop('rank')
except KeyError:
	pass # Handle the case where the key doesn't exist

# Print the updated dictionary
print(user)
