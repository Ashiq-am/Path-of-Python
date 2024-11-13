# Python3 code to demonstrate
# Reverse sort Matrix Row by Kth Column
# using sort() + itemgetter()
from operator import itemgetter

# Initializing list
test_list = [['Manjeet', 65], ['Akshat', 42], ['Akash', 38], ['Nikhil', 192]]

# printing original lists
print("The original list is : " + str(test_list))

# Initializing K
K = 1

# Reverse sort Matrix Row by Kth Column
# using sort() + itemgetter()
test_list.sort(key = itemgetter(K), reverse = True)

# printing result
print ("List after performing sorting of matrix records : " + str(test_list))
