# Python code to demonstrate the
# use of mode() function

# mode() function a sub-set of the statistics module
# We need to import statistics module before doing any work
import statistics

# declaring a simple data-set consisting of real valued
# positive integers.
set1 =[1, 2, 3, 3, 4, 4, 4, 5, 5, 6]

# In the given data-set
# Count of 1 is 1
# Count of 2 is 1
# Count of 3 is 2
# Count of 4 is 3
# Count of 5 is 2
# Count of 6 is 1
# We can infer that 4 has the highest population distribution
# So mode of set1 is 4

# Printing out mode of given data-set
print("Mode of given data set is % s" % (statistics.mode(set1)))
