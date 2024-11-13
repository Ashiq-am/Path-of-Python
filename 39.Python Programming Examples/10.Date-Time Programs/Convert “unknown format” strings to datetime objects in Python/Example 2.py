# Python3 code to illustrate the conversion of
# "unknown format" strings to DateTime objects

# Importing parser from the dateutil.parser and
# dt from datetime module
import dateutil.parser as parser
import datetime as dt

# Calling the now() function to
# return the current datetime
now = dt.datetime.now()

# Calling the isoformat() to return the
# current datetime in isoformat and print it
print(now.isoformat())

# Now calling the parser to parse the
# above returned isoformat datetime into
# a valid known format of datetime object
print(parser.parse(now.isoformat()))
