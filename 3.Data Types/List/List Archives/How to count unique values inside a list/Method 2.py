# importing Counter module
from collections import Counter


input_list = [1, 2, 2, 5, 8, 4, 4, 8]

# creating a list with the keys
items = Counter(input_list).keys()
print("No of unique items in the list are:", len(items))
