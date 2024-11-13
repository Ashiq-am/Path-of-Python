# function to find the armstrong number
def is_armstrong(number):
    digits = str(number)
    # calculate the length of the digit
    length = len(digits)
    # calculate the sum of digits each raised to the power of length
    sum_of_powers = sum(int(digit) ** length for digit in digits)
    # check if the sum of powers is equal to the original number
    return sum_of_powers == number


# function to find armstrong number
def find_armstrong_numbers(start, end):
    # list con=mprehension
    return [num for num in range(start, end + 1) if is_armstrong(num)]


start = 100
end = 500

armstrong_numbers = find_armstrong_numbers(start, end)
print(f"Armstrong numbers between {start} and {end} are: {armstrong_numbers}")
