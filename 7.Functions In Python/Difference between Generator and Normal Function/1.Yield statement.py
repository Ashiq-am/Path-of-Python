# generator function
def Square():
    number = 2

    # Create infinite loop
    while True:
        # Yield the current value of 'number'
        yield number

        # Calculate the square of 'number' and update its value
        number *= number


# Create a generator object 'Sq' by calling the 'Square()' generator function
Sq = Square()

# Function call
print(next(Sq))  # Output: 2

print(next(Sq))  # Output: 4
