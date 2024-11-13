# Input dictionary
profession = {'name': ['Barry', 'Bruce'],
              'profession': ['Engineer', 'Doctor'],
              'age': [30, 31]}

# Use of format_map() function
print('{name[0]} is an {profession[0]} and he'
      ' is {age[0]} years old.'.format_map(profession))

print('{name[1]} is an {profession[1]} and he'
      ' is {age[1]} years old.'.format_map(profession))
