# Python code to demonstrate the working of
# median_grouped()

# importing statistics to handle statistical operations
import statistics

# initializing list
li = [1, 2, 2, 3, 3, 3]

# using median_grouped() to calculate 50th percentile
print ("The 50th percentile of data is : ",end="")
print (statistics.median_grouped(li))
