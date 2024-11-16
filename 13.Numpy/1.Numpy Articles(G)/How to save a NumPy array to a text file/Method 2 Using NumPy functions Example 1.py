# Program to save a NumPy array to a text file

# Importing required libraries
import numpy

# Creating an array
List = [1, 2, 3, 4, 5]
Array = numpy.array(List)

# Displaying the array
print('Array:\n', Array)

# Saving the array in a text file
numpy.savetxt("file1.txt", Array)

# Displaying the contents of the text file
content = numpy.loadtxt('file1.txt')
print("\nContent in file1.txt:\n", content)
