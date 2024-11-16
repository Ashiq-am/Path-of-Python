# import module
import numpy


# explicit function to calculate
# number of days
def calcDays(month, year):
	date = 0

	# December case
	if month == 12:
		end = str(year)+'-'+str(month)+'-31'
		begin = str(year)+'-'+str(month)+'-01'
		date = 1
	else:

		# single digit months
		if month < 10:
			endM = '-0'+str(month+1)
			beginM = '-0'+str(month)

		# double digit months
		else:
			endM = '-'+str(month+1)
			beginM = '-'+str(month)

		end = str(year)+endM+'-01'
		begin = str(year)+beginM+'-01'

	# return number of days
	return (numpy.datetime64(end) - numpy.datetime64(begin)+date)


# Driver Code

# get month
month = 4

# get year
year = 2001

# call the function
print(calcDays(month, year))
