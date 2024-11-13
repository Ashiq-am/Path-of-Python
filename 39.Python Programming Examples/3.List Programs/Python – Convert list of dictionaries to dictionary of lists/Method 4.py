# import numpy module
import numpy as np

# create numpy data
data = np.array([(10, 20), (50, 60)],
				dtype=[('value1', int),
					('value2', int)])

# display by using index
print(data[0])

# display by uing key
print(data['value1'])
