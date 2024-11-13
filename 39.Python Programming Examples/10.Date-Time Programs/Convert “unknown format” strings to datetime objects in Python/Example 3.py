# Python3 code to illustrate the conversion of
# "unknown format" strings to DateTime objects

# Importing parser from the dateutil.parser
import dateutil.parser as parser

# Now parsing the "10-09-2021" datetime with
# dayfirst parameter
B = parser.parse("10-09-2021", dayfirst = True)

# Printing the parsed datetime
print(B)
