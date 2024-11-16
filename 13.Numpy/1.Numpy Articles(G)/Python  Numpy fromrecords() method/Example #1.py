# import numpy
import numpy as np

# using numpy.core.fromrecords() method
gfg = np.core.records.fromrecords([(101, 'Jitender', 21),
									(102, 'Deepak', 20)],
							names = 'Rollno, Name, Age')

print(gfg[0])
