# Moment
from scipy import stats
import numpy as np

arr1 = np.array([[1, 31, 27, 13, 21, 9],
				[8, 12, 8, 4, 7, 10]])


print("Oth moment : \n", stats.moment(arr1, moment = 0))
