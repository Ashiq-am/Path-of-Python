from datetime import date
import holidays

# Select country
uk_holidays = holidays.UnitedKingdom()

# If it is a holidays then it returns True else False
print('01-01-2018' in uk_holidays)
print('02-01-2018' in uk_holidays)

# What holidays is it?
print(uk_holidays.get('01-01-2018'))
print(uk_holidays.get('02-01-2018'))
