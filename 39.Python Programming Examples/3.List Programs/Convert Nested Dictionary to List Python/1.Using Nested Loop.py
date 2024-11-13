# Initiating dictionary
dictionary = {"a":{"b":"c"}}

l = []

# converting dictionary values to list
for k,v in dictionary.items():
    for i,j in v.items():
        l.extend([k, i, j])

print(type(dictionary))
print(l)
print(type(l))
