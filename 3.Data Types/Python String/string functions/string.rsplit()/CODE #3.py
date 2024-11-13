word = 'geeks for geeks'

# Since seperator is 'None',
# so, will be splitted at space
print(word.rsplit(None, 1))

print(word.rsplit(None, 2))

# Also observe these
print('@@@@@geeks@for@geeks'.rsplit('@'))
print('@@@@@geeks@for@geeks'.rsplit('@', 1))
print('@@@@@geeks@for@geeks'.rsplit('@', 3))
print('@@@@@geeks@for@geeks'.rsplit('@', 5))
