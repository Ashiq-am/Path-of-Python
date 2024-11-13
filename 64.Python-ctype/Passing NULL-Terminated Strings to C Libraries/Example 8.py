import sys
s = 'Spicy Jalape\u00f1o'
print ("Size : ", sys.getsizeof(s))

# passing string
print("\n", print_chars(s))

# increasing size
print ("\nSize : ", sys.getsizeof(s))
