from collections import OrderedDict


ord_dict = OrderedDict().fromkeys('GeeksForGeeks')
print("Original Dictionary")
print(ord_dict)

# Pop the key from last
ord_dict.popitem()
print("\nAfter Deleting Last item :")
print(ord_dict)

# Pop the key from beginning
ord_dict.popitem(last = False)
print("\nAfter Deleting Key from Beginning :")
print(ord_dict)
