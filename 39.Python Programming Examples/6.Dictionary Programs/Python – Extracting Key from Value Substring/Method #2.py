# Python3 code to demonstrate working of
# Extracting Key from Value Substring
# Using list comprehension

# initializing dictionary
test_dict = {1: 'Gfg is good', 2: 'Gfg is best', 3: 'Gfg is on top'}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# initializing search_word
srch_wrd = 'best'

# Extracting Key from Value Substring
# Using list comprehension
res = [key for key, val in test_dict.items() if srch_wrd in val]

# printing result
print("The Corresponding key : " + str(res))
