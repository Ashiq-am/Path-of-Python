# Python code to finding number of
# leap years in list of years.

# Input list initialization
Input = [2001, 2002, 2003, 2004, 2005, 2006,
		2007, 2008, 2009, 2010, 2011, 2012]

# Find whether it is leap year or not
def checkYear(year):
	return (((year % 4 == 0) and
			(year % 100 != 0)) or
			(year % 400 == 0))

# Answer Initialization
Answer = 0

for elem in Input:
	if checkYear(elem):
		Answer = Answer + 1

# Printing
print("No of leap years are:", Answer)
