# importing required packages
import pandas
import numpy

Nan = numpy.nan

# creating a dataframe with some nan values
df = pandas.DataFrame(data = numpy.array(
					[[9, -3.4, Nan, 9, Nan],
					[9, 4.89, -3.4, Nan, 9],
					[Nan, -3.4, Nan, 9, 56],
					[4, -3.4, 59.0, 5.6, 90],
					[-4, Nan, Nan, 34, 8.8]]),
					columns = list("ABCDE"))

# view dataframe
df
