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

# Calling the isoformat() function to convert the
# above returned datetime.date object into the
# ISO format date string
string_date = date_object.isoformat()

# Getting the converted date string as output
print(string_date)

# Getting the type of returned date format
print(type(string_date))
