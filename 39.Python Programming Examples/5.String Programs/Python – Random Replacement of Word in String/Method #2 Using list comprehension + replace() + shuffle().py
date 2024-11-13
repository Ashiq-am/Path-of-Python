# Python3 code to demonstrate working of
# Random Replacement of Word in String
# Using list comprehension + replace() + shuffle()
from random import shuffle

# initializing string
test_str = "Gfg is val. Its also val for geeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing list
repl_list = ["Good", "Better", "Best"]

# initializing replace word
repl_word = "val"

# one-liner to solve problem
shuffle(repl_list)
res = [test_str.replace(repl_word, ele, 1) for ele in repl_list]

# printing result
print("String after random replacement : " + str(res))
