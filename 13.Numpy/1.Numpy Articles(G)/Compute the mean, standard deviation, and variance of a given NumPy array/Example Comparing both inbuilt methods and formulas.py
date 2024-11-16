import numpy as np

# Original array
x = np.arange(5)
print(x)

r11 = np.mean(x)
r12 = np.average(x)
print("\nMean: ", r11, r12)

r21 = np.std(x)
r22 = np.sqrt(np.mean((x - np.mean(x)) ** 2))
print("\nstd: ", r21, r22)

r31 = np.var(x)
r32 = np.mean((x - np.mean(x)) ** 2)
print("\nvariance: ", r31, r32)
