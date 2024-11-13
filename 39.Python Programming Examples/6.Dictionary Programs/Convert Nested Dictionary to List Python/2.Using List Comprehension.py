# Initiating dictionary
dictionary = {"a": {"b": "c"}, "d": {"e": "f"}}

# converting dictionary values to list
l = [p for k, v in dictionary.items() for i, j in v.items() for p in (k, i, j)]

print(type(dictionary))
print(l)
print(type(l))
