# import pandas
import pandas

# import numpy
import numpy

# create a dataframe
dataframe = pandas.DataFrame({'name': ['sireesha', 'gnanesh',
									'sridevi', 'vijay', 'sreemukhi'],
							'marks': [90.3, numpy.nan, 67.8, 89, numpy.nan]})

# convert to integer type
dataframe['marks'].astype(int)
