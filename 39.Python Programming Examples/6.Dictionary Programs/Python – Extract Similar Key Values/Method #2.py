# Python3 code to demonstrate working of
# Extract Similar Key Values
# Using list comprehension + sorted()

# initializing dictionary
test_dict = {'gfg': 5, 'ggf': 19, 'gffg': 9, 'gff': 3, 'fgg': 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing word
tst_wrd = 'fgg'

# one-liner to solve this
res = [val for key, val in test_dict.items(
) if ''.join(list(sorted(key))) == tst_wrd]

# printing result
print("The extracted keys : " + str(res))
