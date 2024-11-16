# Change the dtype of the country
# object to 'U256'
country = country.astype('U256')

# Assign 'New Zealand' to the missing value
country[country == ''] = 'New Zealand'

# Print the array
print(country)
