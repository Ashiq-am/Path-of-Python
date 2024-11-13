# Python program to print the hexadecimal value of the
# numbers from 1 to N

# Function to find the hexadecimal value of the numbers
# in the range 1 to N
def hex_in_range(n):
    # For loop traversing from 1 to N (Both Inclusive)
    for i in range(1, n + 1):
        # Printing hexadecimal value of i
        print(hex(i)[2:])

    # Calling the function with input 3


print("Input: 3")
hex_in_range(3)

# Calling the function with input 11
print("Input: 11")
hex_in_range(11)
