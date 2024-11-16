# Python Program illustrating
# numpy.delete()
print("Original arr:", arr)
print("Shape : ", arr.shape)

# deletion from 1D array
object = 2
a = np.delete(arr, object)
print("\ndeleteing the value at index {} from array:\n {}".format(object,a))
print("Shape : ", a.shape)
