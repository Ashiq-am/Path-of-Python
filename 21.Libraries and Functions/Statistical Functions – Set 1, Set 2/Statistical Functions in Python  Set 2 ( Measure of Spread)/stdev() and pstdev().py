# Python code to demonstrate the working of
# stdev() and pstdev()

# importing statistics to handle statistical operations
import statistics

# initializing list
li = [1.5, 2.5, 2.5, 3.5, 3.5, 3.5]

# using stdev to calculate standard deviation of data
print ("The standard deviation of data is : ",end="")
print (statistics.stdev(li))

# using pstdev to calculate population standard deviation of data
print ("The population standard deviation of data is : ",end="")
print (statistics.pstdev(li))
