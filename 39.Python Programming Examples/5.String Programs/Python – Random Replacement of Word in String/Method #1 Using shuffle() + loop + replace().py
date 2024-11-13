# Python3 code to demonstrate working of
# Random Replacement of Word in String
# Using replace() + shuffle() + loop
from random import shuffle

# initializing string
test_str = "Gfg is val. Its also val for geeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing list
repl_list = ["Good", "Better", "Best"]

# initializing replace word
repl_word = "val"

# shuffing list order
shuffle(repl_list)
for ele in repl_list:
    # replacing with random string
    test_str = test_str.replace(repl_word, ele, 1)

# printing result
print("String after random replacement : " + str(test_str))
