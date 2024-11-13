# initializing list
test_list = ["Gfg", "+", "is", "best", "+", "love", "gfg"]

# printing original list
print("The original list is : " + str(test_list))

# initializing K for Concatenate
K = "+"

# performing split after removing space around K
# splits assuming Strings joined around K
res = ' '.join(test_list).replace(' ' + K + ' ', K).split()

# printing result
print("Strings after required concatenation : " + str(res))
