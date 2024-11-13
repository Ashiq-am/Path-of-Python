# Program to illustrate the use of kwargs in Python

# Function that print the details of a student
# The number of details per student may vary
def printDetails(**details):
    # Variable 'details' contains the details in the
    # form of dictionary
    print("Parameter details contains")
    print(details)
    print("Type = ", type(details))

    # Print first name
    print("First Name = ", details['firstName'])

    # Print the department of student
    print("Department = ", details['department'])
    print("")  # Extra line break


# Driver program to test above function

# Calling the function with three arguments
printDetails(firstName="Nikhil",
             rollNumber="007",
             department="CSE")

# Calling the function with two arguments
printDetails(firstName="Abhay",
             department="ECE")












"""Please note that if you are using both args and kwargs in a function then the args 
parameter must precede before the kwarg parameters."""
