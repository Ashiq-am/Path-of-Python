def checkIsPerfectNumber(number):
	divisors = sum([i for i in range(1, number) if number % i == 0])
	return number == divisors

input_Number_is = 6

if checkIsPerfectNumber(input_Number_is):
	print("Number is a Perfect Number.")
else:
	print("Number is not a Perfect Number.")
