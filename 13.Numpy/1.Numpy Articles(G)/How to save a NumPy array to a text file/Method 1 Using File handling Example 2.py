# Program to save a NumPy array to a text file

# Importing required libraries
import numpy

# Creating 2D array
List = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Array = numpy.array(List)

# Displaying the array
print('Array:\n', Array)
file = open("file2.txt", "w+")

# Saving the 2D array in a text file
content = str(Array)
file.write(content)
file.close()

# Displaying the contents of the text file
file = open("file2.txt", "r")
content = file.read()

print("\nContent in file2.txt:\n", content)
file.close()
