# Python code to demonstrate the working of
# mean() and mode()

# importing statistics to handle statistical operations
import statistics

# initializing list
li = [1, 2, 3, 3, 2, 2, 2, 1]

# using mean() to calculate average of list elements
print ("The average of list values is : ",end="")
print (statistics.mean(li))

# using mode() to print maximum occurring of list elements
print ("The maximum occurring element is : ",end="")
print (statistics.mode(li))
