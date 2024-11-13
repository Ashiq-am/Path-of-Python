def is_leap_year_modulo(year):
	return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example
year_to_check = 2024
result_modulo = is_leap_year_modulo(year_to_check)
print(f"{year_to_check} is a leap year: {result_modulo}")
