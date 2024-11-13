is_leap_year_lambda = lambda year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example
year_to_check = 2023
result_lambda = is_leap_year_lambda(year_to_check)
print(f"{year_to_check} is a leap year: {result_lambda}")
