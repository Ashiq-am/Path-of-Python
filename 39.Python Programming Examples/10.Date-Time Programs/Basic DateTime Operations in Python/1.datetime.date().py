from datetime import date

# You can create a date object containing
# the current date
# by using a classmethod named today()
current = date.today()

# print current year, month, and year individually
print("Current Day is :", current.day)
print("Current Month is :", current.month)
print("Current Year is :", current.year)

# strftime() creates string representing date in
# various formats
print("\n")
print("Let's print date, month and year in different-different ways")
format1 = current.strftime("%m/%d/%y")

# prints in month/date/year format
print("format1 =", format1)

format2 = current.strftime("%b-%d-%Y")
# prints in month(abbreviation)-date-year format
print("format2 =", format2)

format3 = current.strftime("%d/%m/%Y")

# prints in date/month/year format
print("format3 =", format3)

format4 = current.strftime("%B %d, %Y")

# prints in month(words) date, year format
print("format4 =", format4)
