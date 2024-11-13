import calendar

def is_leap_year_calendar(year):
	return calendar.isleap(year)

# Example
year_to_check = 2024
result_calendar = is_leap_year_calendar(year_to_check)
print(f"{year_to_check} is a leap year: {result_calendar}")
