# Python code to demonstrate the working of
# variance() and pvariance()

# importing statistics to handle statistical operations
import statistics

# initializing list
li = [1.5, 2.5, 2.5, 3.5, 3.5, 3.5]

# using variance to calculate variance of data
print ("The variance of data is : ",end="")
print (statistics.variance(li))

# using pvariance to calculate population variance of data
print ("The population variance of data is : ",end="")
print (statistics.pvariance(li))
