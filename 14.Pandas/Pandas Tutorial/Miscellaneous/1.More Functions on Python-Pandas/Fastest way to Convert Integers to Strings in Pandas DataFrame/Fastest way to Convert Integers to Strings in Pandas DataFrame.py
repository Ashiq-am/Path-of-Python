import pandas as pd
import sys
import time
import numpy as np

print('Version Of Python: ' + sys.version)
print('Version Of Pandas: ' + pd.__version__)
print('Version Of Numpy: ' + np.version.version)

frame1 = pd.DataFrame(np.random.randint(0, 90, size =(5000000, 1)), columns =['random'])
frame2 = pd.DataFrame(np.random.randint(0, 90, size =(5000000, 1)), columns =['random'])
frame3 = pd.DataFrame(np.random.randint(0, 90, size =(5000000, 1)), columns =['random'])
frame4 = pd.DataFrame(np.random.randint(0, 90, size =(5000000, 1)), columns =['random'])


# Using map(str) method
t1 = time.time()
frame1['random'] = frame1['random'].map(str)
output1 = (time.time() - t1)
print('Time taken in seconds using map(str): ' + str(output1))

# Using apply(str) method
t2 = time.time()
frame2['random'] = frame2['random'].apply(str)
output2 = (time.time() - t2)
print('Time taken in seconds using apply(str): ' + str(output2))

# Using astype(str) method
t3 = time.time()
frame3['random'] = frame3['random'].astype(str)
output3 = (time.time() - t3)
print('Time taken in seconds using astype(str): ' + str(output3))

# Using values.astype(str) method
t4 = time.time()
frame4['random'] = frame4['random'].values.astype(str)
output4 = (time.time() - t4)
print('Time taken in seconds using values.astype(str): ' + str(output4))

l =[output1, output2, output3, output4]
m =['map(str)', 'apply(str)', 'astype(str)', 'values.astype(str)']

# Fastest way to convert into string
minimum = min(l)
k = l.index(minimum)
fastest = m[k]

# It will print the fastest conversion method.
print(fastest+" is the fastest method")
