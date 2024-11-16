import numpy as np

originalVect = np.array([1, 2, 3, 4])

clonedRowVect = np.copy(originalVect)
clonedColumnVect = np.copy(originalVect[:, np.newaxis])

print("Original Row Vector:", originalVect)
print("Cloned Row Vector:", clonedRowVect)
print("Cloned Column Vector:")

print(clonedColumnVect)
