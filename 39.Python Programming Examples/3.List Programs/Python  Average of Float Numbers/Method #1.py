# Python3 code to demonstrate working of
# Average of Float Numbers
# using loop + formula
import math

# initialize list
test_list = [6.1, 7.2, 3.3, 9.4, 10.6, 15.7]

# printing original list
print("The original list is : " + str(test_list))

# Average of Float Numbers
# using loop + formula
sum = 0
for ele in test_list:


    sum += ele

res = sum / len(test_list)

# printing result
print("The mean of float list elements is : " + str(res))
