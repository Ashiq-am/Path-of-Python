# function to find cube
def cube(num):
    # product varib]able
    result = 1

    # for loop
    for _ in range(3):
        result *= num
    return result


num = 5
print(f"The cube of {num} is {cube(num)}")
