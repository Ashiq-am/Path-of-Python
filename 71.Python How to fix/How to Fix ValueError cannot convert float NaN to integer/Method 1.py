# import pandas
import pandas

# import numpy
import numpy

# create a dataframe
dataframe = pandas.DataFrame({'name': ['sireesha', 'gnanesh',
									'sridevi', 'vijay',
									'sreemukhi'],
							'marks': [90.3, numpy.nan, 67.8, 89, numpy.nan]})
# display data type
print(dataframe['marks'] .dtype)


# drop the NaN values
dataframe = dataframe.dropna()

# display
print(dataframe)

# convert to integer type for marks column
dataframe['marks'] = dataframe['marks'].astype(int)

# display data type
dataframe['marks'] .dtype
