# Python program to demonstrate data
# storing similarities in array and list

# importing array module
import array as arr

# Declaring a Homogeneous List of strings
Homogeneous_List = ["Geeks", "For", "Geeks"]
print("List of Strings: ")

# Printing the list
print(Homogeneous_List)

# Declaring a list of
# non-homogeneous elements
Non_homogeneous_list = [10, "Geeks",\
		20.890, "for", 30, "geeks"]
print("List of non-homogeneous elements: ")

# Printing the list
print(Non_homogeneous_list)

# declaring an array of float type
# 'd' signifies integer type and
# elements inside [] are the array elements
Homogeneous_array = arr.array('d',\
				[1.5, 2.4, 3.9])

# printing elements of array
print ("Elements of the array is"\
				" : ", end = " ")
for i in range (len(Homogeneous_array)):
	print (Homogeneous_array[i], end =", ")
