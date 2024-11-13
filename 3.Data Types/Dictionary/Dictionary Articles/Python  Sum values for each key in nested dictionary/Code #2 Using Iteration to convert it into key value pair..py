# Python code to find sum values within nested dictionaries

weapons = {'': None, 'sword': {'steel': 151,
                               'sharpness': 100,
                               'age': 2, },

           'arrow': {'steel': 120,
                     'sharpness': 205,
                     'age': 1, }}

sum = 0

# iterating key value pair
for key, value in weapons.items():

    if value and 'sharpness' in value.keys():
        # Adding value of sharpness to sum
        sum += value['sharpness']

    # printing sum
print(sum)
