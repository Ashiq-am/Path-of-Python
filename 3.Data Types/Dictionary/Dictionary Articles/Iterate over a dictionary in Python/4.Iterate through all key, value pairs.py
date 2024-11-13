# Python3 code to iterate through all key, value
# pairs in a dictionary

statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}

print('List Of given states and their capitals:\n')

# Iterating over values
for state, capital in statesAndCapitals.items():
    print(state, ":", capital)
