# Python3 code to illustrate the conversion of
# datetime.datetime to excel serial date number

# Importing date module from datetime
from datetime import date

# Taking the parameter from the calling function
def convert_date_to_excel_ordinal(day, month, year):

	# Specifing offset value i.e.,
	# the date value for the date of 1900-01-00
	offset = 693594
	current = date(year, month, day)

	# Calling the toordinal() function to get
	# the excel serial date number in the form
	# of date values
	n = current.toordinal()
	return (n - offset)

# Calculating the excel serial date number
# for the date "02-02-2021" by calling the
# user defined function convert_date_to_excel_ordinal()
print(convert_date_to_excel_ordinal(2, 2, 2021))
