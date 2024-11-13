import math


def calculate_logarithm(x):
    try:
        result = math.log(x)

        print("Logarithm result:", result)
    except ValueError as e:

        print(f"Error: {e}")
        print("Invalid input for logarithm")


input_value = 98
calculate_logarithm(input_value)
