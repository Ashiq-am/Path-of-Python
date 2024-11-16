import pandas as pd

#initialize the temperature value at the first day of the month
c = 30

# Create a dataframe using the three lists
# the y-axis variable is a list created using
# a for loops, in each iteration,
# it adds 1 to previous value
# the x-axis variable is a list of values ranging
# from 1 to 31 (31 not included) with a step of 1
df = pd.DataFrame([ c + x for x in range( 0 , 30 )],
				index = [*range( 1 , 31 , 1 )],
				columns = [ 'Temperature (C)' ])

# use plot() method on the dataframe.
# No parameters are passed so it uses
# variables given in the dataframe
df.plot(color='red', title = 'Total Coins per Day')
