# importing libraries
import keyword
import enchant
from itertools import permutations

d = enchant.Dict("en_US")

words = []
perm_word = []

# character combination to
# list down all the words
str_arr = "star"

# Getting the string length to use it in the loop.
str_len = 4
print("Length of the string is : ", str_len)

while str_len > 1:

    if str_len == len(str_arr):
        perm = list(permutations(str_arr))
        str_len = str_len - 1

        for i in list(perm):
            words = ''.join(i)

            if d.check(words):
                perm_word.append(words)
                print(words + " is an English words")
        print("perm_word", perm_word)

    elif str_len > 1:
        perm = list(permutations(str_arr, str_len))
        str_len = str_len - 1

        for i in list(perm):
            words = ''.join(i)

            if d.check(words):
                perm_word.append(words)
                print(words + " is an English word")
        print("perm_word", perm_word)

    else:
        str_len = 0
