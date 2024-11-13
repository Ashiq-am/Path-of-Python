# function to find the armstrong number
def is_armstrong(number):
    digits = str(number)
    # calculate the length of the digit
    length = len(digits)
    # calculate the sum of digits each raised to the power of length
    sum_of_powers = sum(int(digit) ** length for digit in digits)
    # check if the sum of powers is equal to the original number
    return sum_of_powers == number


# function to iterate through the interval
def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    # for loop to iterate through interval
    for num in range(start, end + 1):
        if is_armstrong(num):
            # add armsstrong number in the list
            armstrong_numbers.append(num)
    return armstrong_numbers


start = 100
end = 500

armstrong_numbers = find_armstrong_numbers(start, end)
print(f"Armstrong numbers between {start} and {end} are: {armstrong_numbers}")
