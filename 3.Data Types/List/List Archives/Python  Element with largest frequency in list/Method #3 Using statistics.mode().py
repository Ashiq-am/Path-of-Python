# Python3 code to demonstrate
# to get most frequent element
# using statistics.mode()
import statistics

# initializing list
test_list = [9, 4, 5, 4, 4, 5, 9, 5, 4]

# printing original list
print("Original list : " + str(test_list))

# using statistics.mode() to
# get most frequent element
res = statistics.mode(test_list)

# printing result
print("Most frequent number is : " + str(res))
