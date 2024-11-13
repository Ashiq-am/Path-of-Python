# Python code to demonstrate the working of
# median(), median_low() and median_high()

# importing statistics to handle statistical operations
import statistics

# initializing list
li = [1, 2, 2, 3, 3, 3]

# using median() to print median of list elements
print ("The median of list element is : ",end="")
print (statistics.median(li))

# using median_low() to print low median of list elements
print ("The lower median of list element is : ",end="")
print (statistics.median_low(li))

# using median_high() to print high median of list elements
print ("The higher median of list element is : ",end="")
print (statistics.median_high(li))
