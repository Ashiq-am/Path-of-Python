def IsPerfectNumberFilterMethod(number):

	divisors = list(filter(lambda x: number % x == 0, range(1, number)))
	return sum(divisors) == number

input_Number_is = 25

if IsPerfectNumberFilterMethod(input_Number_is):
	print("Number is a Perfect Number.")
else:
	print("Number is not a Perfect Number.")
