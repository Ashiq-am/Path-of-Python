# Python3 code to demonstrate working of
# Cummulative Row Frequencies
# Using Counter() + list comprehension
from collections import Counter

# initializing list
test_list = [[10, 2, 3, 2, 3],
			[5, 5, 4, 7, 7, 4],
			[1, 2], [1, 1, 2, 2, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing ele_list
ele_list = [1, 2, 7]

# getting each rows counter
freqs = [Counter(ele) for ele in test_list]

# getting summation of present values
res = [sum([freq[wrd] for wrd in ele_list if wrd in freq]) for freq in freqs]

# printing result
print("Cummulative Frequencies : " + str(res))
