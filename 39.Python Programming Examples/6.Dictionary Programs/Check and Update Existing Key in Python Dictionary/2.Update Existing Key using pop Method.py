# Creating a dictionary
user = {'name': 'Geek', 'rank': 10, 'city': 'Geek Town'}

# Updating the key name from 'city' to 'town' and keeping the same value
user['town'] = user.pop('city')

# Displaying the updated dictionary
print(user)
