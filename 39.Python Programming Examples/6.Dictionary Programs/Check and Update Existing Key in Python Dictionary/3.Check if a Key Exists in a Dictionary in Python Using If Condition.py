# Initial dictionary
user = {'name': 'Geek', 'rank': 10, 'city': 'Geek Town'}

# Check if the old key exists before updating
if 'rank' in user:
	# Create a new key with the updated name and the same value
	user['age'] = user.pop('rank')

# Print the updated dictionary
print(user)
