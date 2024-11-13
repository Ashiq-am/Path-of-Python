# Initial dictionary
user = {'name': 'Geek', 'rank': 10, 'city': 'Geek Town'}

# Update existing key using direct assignment
if 'rank' in user:
	user['age'] = user['rank']
	del user['rank']

# Print the updated dictionary
print(user)
