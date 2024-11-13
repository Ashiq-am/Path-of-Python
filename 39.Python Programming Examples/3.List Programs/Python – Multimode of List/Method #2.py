# Python3 code to demonstrate working of
# Multimode of List
# using statistics.multimode()
import statistics

# initialize list
test_list = [1, 2, 1, 2, 3, 4, 3]

# printing original list
print("The original list is : " + str(test_list))

# Multimode of List
# using statistics.multimode()
res = statistics.multimode(test_list)

# printing result
print("The multimode of list is : " + str(res))
