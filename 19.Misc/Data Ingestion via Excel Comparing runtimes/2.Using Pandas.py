import pandas as pd
import time


# Time variable for finding the
# difference
t1 = time.time()

data = pd.read_excel('excel.xls')
print(data.head())

t2 = time.time()
print("\nTime taken by xlrd:")
print(t2-t1)
