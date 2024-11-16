# split(pattern)
print(df)
print('\nAfter using the strip:')
print(df.str.split(','))

# now we can use [] or get() to fetch
# the index values
print('\nusing []:')
print(df.str.split(',').str[0])

print('\nusing get():')
print(df.str.split(',').str.get(1))
