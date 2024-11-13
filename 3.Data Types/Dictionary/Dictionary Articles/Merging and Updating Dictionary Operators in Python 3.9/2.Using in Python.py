# Python code to merge dict
# using a single expression


dict1 = {'a': 10, 'b': 5, 'c': 3}
dict2 = {'d': 6, 'c': 4, 'b': 8}

dict3 = {**dict1,**dict2}

print("dict1 :", dict1)
print("dict2 :", dict2)
print("dict3 :", dict3)
