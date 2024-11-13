# All elements of set are true
s = {1, 1, 3}
print(all(s))

# All elements of set are false
s = {0, 0, False}
print(all(s))

# Some elements of set
# are true while others are false
s = {1, 2, 0, 8, False}
print(all(s))

# Empty set
s = {}
print(all(s))
