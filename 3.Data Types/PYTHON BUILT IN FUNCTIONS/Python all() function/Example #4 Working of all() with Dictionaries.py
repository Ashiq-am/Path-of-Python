# All elements of dictionary are true
d = {1: "Hello", 2: "Hi"}
print(all(d))

# All elements of dictionary are false
d = {0: "Hello", False: "Hi"}
print(all(d))

# Some elements of dictionary
# are true while others are false
d = {0: "Salut", 1: "Hello", 2: "Hi"}
print(all(d))

# Empty dictionary
d = {}
print(all(d))
