from collections import OrderedDict


ord_dict = OrderedDict().fromkeys('GeeksForGeeks')
print("Original Dictionary")
print(ord_dict)

# Move the key to end
ord_dict.move_to_end('G')
print("\nAfter moving key 'G' to end of dictionary :")
print(ord_dict)

# Move the key to beginning
ord_dict.move_to_end('k', last = False)
print("\nAfter moving Key in the Beginning :")
print(ord_dict)
