# declaring dictionary
dict1 = {'hari': 1, 'dita': 2}

# original dictionary
print("initial dictionary-", dict1)

# list of values which will replace the values of dict1
list1 = [3, 5]

# this preserves the keys and modifies the values
dict1 = dict(zip(list(dict1.keys()), list1))

# modified dictionary
print("dictionary after modification-", dict1)
