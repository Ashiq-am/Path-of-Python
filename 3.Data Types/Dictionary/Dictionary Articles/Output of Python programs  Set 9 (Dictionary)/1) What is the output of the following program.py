dictionary = {'GFG' : 'geeksforgeeks.org',
			'google' : 'google.com',
			'facebook' : 'facebook.com'
			}
del dictionary['google']
for key, values in dictionary.items():
	print(key)
dictionary.clear()
for key, values in dictionary.items():
	print(key)
del dictionary
for key, values in dictionary.items():
	print(key)
