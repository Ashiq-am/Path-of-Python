# Python 3.9 code explaining
# str.removeprefix()

s = 'GeeksforGeeks'

# prefix exists
print(s.removeprefix('Geeks'))
print(s.removeprefix('G'))


# whole string is a prefix
# it would print an empty string
print(s.removeprefix('GeeksforGeeks'))

# prefix doesn't exist
# whole string is returned
print(s.removeprefix('for'))
print(s.removeprefix('IT'))
print(s.removeprefix('forGeeks'))
