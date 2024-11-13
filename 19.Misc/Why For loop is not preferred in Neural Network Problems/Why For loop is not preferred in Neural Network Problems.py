import numpy as np
import time


a = np.array([1, 2, 3, 4])

# there will be 100000 training data
a = np.random.rand(100000)
b = np.random.rand(100000)

# FOR VECTORIZTION
# Measure current time
time1 = time.time()

# computing
c = np.dot(a, b)

# Measure current time
time2 = time.time()

# printing time taken for above calculation
print("vectorized form time taken"+ "\t"+str(1000*(time2-time1))+"ms")

# FOR for loop
# measure current time
time3 = time.time()
c = 0

# computing
for i in range(100000):
    c+= a[i]*b[i]

# measure current time
time4 = time.time()

# printing time taken for above calculation
print("for loop time taken "+"\t\t"+str(1000*(time4-time3))+"ms")
