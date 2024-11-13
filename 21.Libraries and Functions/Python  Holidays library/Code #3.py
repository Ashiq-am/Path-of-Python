from datetime import date
import holidays

# Combining Countries
north_america = holidays.CA() + holidays.US() + holidays.MX()
# Output list of countries combined
print(north_america.country)

print(north_america.get('07-01-2018'))
print(north_america.get('07-04-2018'))
