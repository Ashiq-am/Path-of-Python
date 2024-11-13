# All elements of set are True
s = { 1, 1, 3}
print(any(s))

# All elements of set are False
s = { 0, 0, False}
print(any(s))

# Some elements of set are True while others are False
s = { 1, 2, 0, 8, False}
print(any(s))

# Empty set
s = {}
print(any(s))
