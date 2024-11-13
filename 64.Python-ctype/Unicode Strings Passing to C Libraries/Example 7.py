import sys

s = 'Spicy Jalape\u00f1o'
print ("Size : ", sys.getsizeof(s))

print("\n", print_chars(s))

print ("\nSize : ", sys.getsizeof(s))

print ("\n", print_wchars(s))

print ("\nSize : ", sys.getsizeof(s))
