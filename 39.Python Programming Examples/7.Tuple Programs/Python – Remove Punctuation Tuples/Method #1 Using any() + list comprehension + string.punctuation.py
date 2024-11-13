# Python3 code to demonstrate working of
# Remove Punctuation Tuples
# Using any() + list comprehension + string.punctuation
import string

# initializing list
test_list = [('.', ', '), ('!', 8), (5, 6), (';', 10)]

# printing original list
print("The original list is : " + str(test_list))

# Remove Punctuation Tuples
# Using any() + list comprehension + string.punctuation
res = [idx for idx in test_list if not any(punc in idx
                                           for punc in string.punctuation)]

# printing result
print("Tuples after punctuation removal : " + str(res))
