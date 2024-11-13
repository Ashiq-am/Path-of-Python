# Python code to demonsrate the working of
# interval in median_grouped() function

# importing statistics module
from statistics import median_grouped

# creating a tuple of simple data
set1 = (10, 12, 13, 12, 13, 15)

# Printing median_grouped()
# keeping default interval at 1
print("Grouped Median for Interval set as "\ 
	"(default) 1 is % s" %(median_grouped(set1)))

# For interval value of 2
print("Grouped Median for Interval set as "\ 
	"2 is % s" %(median_grouped(set1, interval = 2)))

# Now for interval value of 5
print("Grouped Median for Interval set as "\ 
	"5 is % s" %(median_grouped(set1, interval = 5)))
