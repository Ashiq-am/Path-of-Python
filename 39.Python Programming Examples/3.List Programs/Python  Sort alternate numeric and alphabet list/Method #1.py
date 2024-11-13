# Python3 code to demonstrate
# Sort alternate numeric and alphabet list
# using isalpha() + isnumeric() + zip_longest()
from itertools import zip_longest

# Initializing list
test_list = ['3', 'B', '2', 'A', 'C', '1']

# printing original list
print("The original list is : " + str(test_list))

# Sort alternate numeric and alphabet list
# using isalpha() + isnumeric() + zip_longest()
num_list = sorted(filter(str.isnumeric, test_list),
                  key=lambda sub: int(sub))

chr_list = sorted(filter(str.isalpha, test_list))
res = [ele for sub in zip_longest(num_list, chr_list)
       for ele in sub if ele]

# printing result
print("List after performing sorting : " + str(res))
