# Initialising a dictionary
my_dict = {"b": 2, "c": 3, "a": 1,"d":4}

# Reverse sorting a dictionary
sorted_dict = sorted(my_dict, reverse=True)

# Printing dictionary
print("Sorted dictionary is :")

for k in sorted_dict:
    print(k,':',my_dict[k])
