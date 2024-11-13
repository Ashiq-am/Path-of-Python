# import pandas
import pandas

# import numpy
import numpy

# create a dataframe
dataframe = pandas.DataFrame({'name': ['sireesha', 'gnanesh',
									'sridevi', 'vijay',
									'sreemukhi'],
							'marks': [90.3, numpy.NaN, 67.8, 89, numpy.NaN]})
# display data type
print(dataframe['marks'] .dtype)

# replace NaN values with 0
dataframe = dataframe.fillna(0)

# display
print(dataframe)

# convert to integer type for marks column
dataframe['marks'] = dataframe['marks'].astype(int)

# display data type
dataframe['marks'] .dtype
