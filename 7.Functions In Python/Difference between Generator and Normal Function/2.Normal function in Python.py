# generator function named square()
def square():
    number = 2

    # Create infinite loop
    while True:
        # Yield the current value of 'number'
        yield number

        # Calculate the square of 'number' and update its value
        number *= number


# Define a function to retrieve the next square from the generator.
def get_next_square():
    global number_generator
    try:
        # Try to get the next square from the existing generator
        return next(number_generator)
    except NameError:
        # If 'number_generator' is not defined , initialize it
        number_generator = square()

        # Return the first square from the newly created generator.
        return next(number_generator)


# function call to retrieve the next square and print it.
print(get_next_square())  # Output: 2

print(get_next_square())  # Output: 4
