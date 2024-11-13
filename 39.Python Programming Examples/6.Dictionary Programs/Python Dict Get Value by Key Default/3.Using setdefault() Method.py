# Example using setdefault() method
my_dict = { 'gfg': 3, 'geeks': 5, 'for': 2, 'geek': 4, 'tutorial': 8}

# Using setdefault() with a default value of 0
value = my_dict.setdefault('geek', 0)
print("value of the key",value)
