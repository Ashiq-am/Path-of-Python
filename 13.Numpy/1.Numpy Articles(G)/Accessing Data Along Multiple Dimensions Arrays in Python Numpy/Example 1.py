# 1-dimensional array
from pandas import np

array1D = np.array([1, 2, 3, 4, 5])

print(array1D)

# to access elements using positive
# index
print("\nusing positive index :" +str(array1D[0]))
print("using positive index :" +str(array1D[4]))

# negative indexing works in opposite
# direction
print("\nusing negative index :" +str(array1D[-5]))
print("using negative index :" +str(array1D[-1]))
