# Python3 code
# Implementing Linear interpolation
# Creating Function to calculate the
# linear interpolation

def interpolation(d, x):
	output = d[0][1] + (x - d[0][0]) * ((d[1][1] - d[0][1])/(d[1][0] - d[0][0]))

	return output

# Driver Code
data=[[2019, 12124],[2021, 5700]]

year_x=2020

# Finding the interpolation
print("Population on year {} is".format(year_x),
			interpolation(data, year_x))
