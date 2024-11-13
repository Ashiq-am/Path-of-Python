# Python3 code to demonstrate working of
# Convert Matrix to Dictionary Value List
# Using dictionary comprehension + zip()
from collections import defaultdict

# initializing list
test_list = [[4, 5, 6], [1, 3, 5], [3, 8, 1], [10, 3, 5]]

# printing original list
print("The original list is : " + str(test_list))

# initializing map list
map_list = [4, 5, 6]

# mapping column using zip(), dictionary comprehension for key
# converts to list of dictionary
temp = [{key: val for key,
                      val in zip(map_list, idx)} for idx in test_list]

# convert to dictionary value list
res = defaultdict(list)
{res[key].append(sub[key]) for sub in temp for key in sub}

# printing result
print("Converted Dictionary : " + str(dict(res)))
