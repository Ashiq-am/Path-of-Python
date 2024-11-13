# Python3 code to demonstrate
# insertion in sorted list
# using bisect.insort()
import bisect

# initializing list
test_list = [1, 2, 3, 6, 7]

# printing original list
print ("The original list is : " + str(test_list))

# insert element
k = 5

# using bisect.insort()
# insertion in sorted list
# using naive method
bisect.insort(test_list, k)

# printing result
print ("The list after insertion is : " + str(test_list))
