# Python3 code to demonstrate working of
# Average of Float Numbers
# using statistics.fmean()
import statistics

# initialize list
test_list = [6.1, 7.2, 3.3, 9.4, 10.6, 15.7]

# printing original list
print("The original list is : " + str(test_list))

# Average of Float Numbers
# using statistics.fmean()
res = statistics.fmean(test_list)

# printing result
print("The mean of float list elements is : " + str(res))
