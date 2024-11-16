# Defining ndarray
from pandas import np

x = np.array([1, 2])
y = np.array([4, 9, 5, 4])

quotient, remainder = np.polydiv(y, x)

print("quotient : ", quotient)
print("remainder : ", remainder)
