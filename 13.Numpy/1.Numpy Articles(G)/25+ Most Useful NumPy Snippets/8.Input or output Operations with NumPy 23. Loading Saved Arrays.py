# Loading the saved binary array
loaded_array = np.load('array.npy')
print("Loaded Array from Binary File:\n", loaded_array)

# Loading the saved text array
loaded_text_array = np.loadtxt('array.txt', delimiter=',')
print("Loaded Array from Text File:\n", loaded_text_array)