def check_number(a):
	if a > 2:
		if a < 7:
			return "Number is between 2 and 7"
		return "Number is greater than 2"
	return "Number is out of the range of 2 and 7"

a = 5
result = check_number(a)
print(result)
