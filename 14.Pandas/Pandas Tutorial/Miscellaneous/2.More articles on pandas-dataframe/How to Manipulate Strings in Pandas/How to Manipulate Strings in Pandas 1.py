# find firstname starting with 'D'
result = cfile.FirstName.str.startswith('D')
print(result)

# find lasttname containing 'XX'
result = cfile.LastName.str.contains('XX')
print(result)


# split FirstName on the basis of ' '
result = cfile.FirstName.str.split()
print(result)


# find length of lasttname
result = cfile.LastName.str.len()
print(result)

# Capitalize the first Letter of LastName
result = cfile.LastName.str.capitalize()
print(result)

# Capitalize all Letter of LastName
result = cfile.LastName.str.upper()
print(result)

# Convert all Letter of LastName to lowercase
result = cfile.LastName.str.lower()
print(result)
