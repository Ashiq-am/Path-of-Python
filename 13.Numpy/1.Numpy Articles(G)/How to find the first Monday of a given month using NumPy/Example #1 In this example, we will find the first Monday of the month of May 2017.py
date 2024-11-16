# import module
import numpy

# input year and month
yearMonth = '2017-05'

# getting date of first monday
date = numpy.busday_offset(yearMonth, 0,
						roll='forward',
						weekmask='Mon')

# display date
print(date)
