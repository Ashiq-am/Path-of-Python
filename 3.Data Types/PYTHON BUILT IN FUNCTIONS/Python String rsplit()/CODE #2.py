word = 'geeks, for, geeks, pawan'

# maxsplit: 0
print(word.rsplit(', ', 0))

# maxsplit: 4
print(word.rsplit(', ', 4))

word = 'geeks@for@geeks@for@geeks'

# maxsplit: 1
print(word.rsplit('@', 1))

# maxsplit: 2
print(word.rsplit('@', 2))
