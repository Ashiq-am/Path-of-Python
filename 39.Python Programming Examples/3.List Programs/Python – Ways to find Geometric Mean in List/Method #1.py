# Python3 code to demonstrate working of
# Geometric Mean of List
# using loop + formula
import math

# initialize list
test_list = [6, 7, 3, 9, 10, 15]

# printing original list
print("The original list is : " + str(test_list))

# Geometric Mean of List
# using loop + formula
temp = 1
for i in range(0, len(test_list)) :
	temp = temp * test_list[i]
temp2 = (float)(math.pow(temp, (1 / len(test_list))))
res = (float)(temp2)

# printing result
print("The geometric mean of list is : " + str(res))
