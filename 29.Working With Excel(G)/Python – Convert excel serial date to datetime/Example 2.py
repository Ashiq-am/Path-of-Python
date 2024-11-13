# Python3 code to illustrate the conversion
# of excel serial date to datetime

# Importing xlrd module
import xlrd

# Initializing an excel serial date
xl_date = 43831

# Calling the xldate_as_datetime() function to
# convert the specified excel serial date into
# datetime.datetime object
datetime_date = xlrd.xldate_as_datetime(xl_date, 0)

# Calling the datetime_date.date() function to convert
# the above returned datetime.datetime object into
# datetime.date object
date_object = datetime_date.date()

# Getting the converted date date as output
print(date_object)

# Getting the type of returned date format
print(type(date_object))
