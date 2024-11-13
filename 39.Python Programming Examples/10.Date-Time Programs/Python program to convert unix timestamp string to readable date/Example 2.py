# Python program to illustrate the
# convertion of unix timestamp string
# to its readable date

# Importing datetime module
import datetime

# Calling the fromtimestamp() funtion to
# extact datetime from the given timestamp
timestamp = datetime.datetime.fromtimestamp(1200001234)

# Calling the strftime() function to convert
# the extracted datetime into its string format
print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
