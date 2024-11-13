# Python code to finding number of
# leap years in list of years.

# Importing calender
import calendar

# Input list initialization
Input = [2001, 2002, 2003, 2004, 2005,
		2006, 2007, 2008, 2009, 2010]

# Using calender to find leap year
def FindLeapYear(Input):
	ans = 0
	for elem in Input:
		if calendar.isleap(int(elem)):
			ans = ans + 1
	return ans

Output = FindLeapYear(Input)

# Printing
print("No of leap years are:", Output)
