# Program to save a NumPy array to a text file

# Importing required libraries
import numpy

# Creating 2D array
List = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Array = numpy.array(List)

# Displaying the array
print('Array:\n', Array)

# Saving the 2D array in a text file
numpy.savetxt("file2.txt", Array)

# Displaying the contents of the text file
content = numpy.loadtxt('file2.txt')
print("\nContent in file2.txt:\n", content)
