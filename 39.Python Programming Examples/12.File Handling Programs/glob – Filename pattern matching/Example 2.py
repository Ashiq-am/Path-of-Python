import glob

# Using character ranges []
print('Finding file using character ranges [] :- ')
print(glob.glob('./[0-9].*'))

# Using wildcard character *
print('\n Finding file using wildcard character * :- ')
print(glob.glob('*.gif'))

# Using wildcard character ?
print('\n Finding file using wildcard character ? :- ')
print(glob.glob('?.gif'))

# Using recursive attribute
print('\n Finding files using recursive attribute :- ')
print(glob.glob('**/*.txt', recursive=True))
