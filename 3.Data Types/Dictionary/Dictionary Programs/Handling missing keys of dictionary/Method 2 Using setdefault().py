country_code = {'India' : '0091',
				'Australia' : '0025',
				'Nepal' : '00977'}

# Set a default value for Japan
country_code.setdefault('Japan', 'Not Present')

# search dictionary for country code of India
print(country_code['India'])

# search dictionary for country code of Japan
print(country_code['Japan'])
