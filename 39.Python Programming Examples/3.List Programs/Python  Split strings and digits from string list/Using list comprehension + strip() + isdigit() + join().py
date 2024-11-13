# Python3 code to demonstrate working of
# Extract digit from string list
# using list comprehension + strip() + isdigit() + join()
from itertools import groupby

# initialize list
test_list = ["-4", "Rs 25", "5 kg", "+15"]

# printing original list
print("The original list : " + str(test_list))

# Extract digit from string list
# using list comprehension + strip() + isdigit() + join()
res = [''.join(j).strip() for sub in test_list
		for k, j in groupby(sub, str.isdigit)]

# printing result
print("List after removing stray characters : " + str(res))
