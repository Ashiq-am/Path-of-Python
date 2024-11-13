string = "geeks is a good"

# 'is' separator is found
print(string.partition('is '))

# 'not' separator is not found
print(string.partition('bad '))

string = "geeks is a good, isn't it"

# splits at first occurrence of 'is'
print(string.partition('is'))
