# FInding statistics of data

from scipy import stats

arr1 = [9, 3, 27]

desc = stats.describe(arr1)

print("No. of observations is :\n", desc)
