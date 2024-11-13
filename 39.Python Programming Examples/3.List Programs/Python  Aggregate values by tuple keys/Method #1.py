# Python3 code to demonstrate working of
# Aggregate values by tuple keys
# using Counter() + generator expression
from collections import Counter

# initialize list
test_list = [('gfg', 50), ('is', 30), ('best', 100),
						('gfg', 20), ('best', 50)]

# printing original list
print("The original list is : " + str(test_list))

# Aggregate values by tuple keys
# using Counter() + generator expression
res = list(Counter(key for key, num in test_list
				for idx in range(num)).items())

# printing result
print("List after grouping : " + str(res))
