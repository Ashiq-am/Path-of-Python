def is_leap_year(year):
	return any([(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)])

# Example
year_to_check = 2018
result_list = is_leap_year(year_to_check)
print(f"{year_to_check} is a leap year: {result_list}")
