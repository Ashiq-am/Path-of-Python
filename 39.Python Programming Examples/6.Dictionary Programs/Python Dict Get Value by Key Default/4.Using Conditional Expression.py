Dictionary ={ 'gfg': 3, 'geeks': 5, 'for': 2, 'geek': 4, 'tutorial': 8}
key = "geek"

#retrieving the value of the provided key using conditional expression
value = Dictionary[key] if key in Dictionary else "None"

print("value of the key", key,"=", value)
