import scipy.io as syio

# Save the mat file
n = 1706256
syio.savemat('num.mat', {'num': n})

# Load the mat File
matlab_file_contents = syio.loadmat('num.mat')
print(matlab_file_contents)

# printing the contents of mat file.
matlab_file_contents = syio.whosmat('num.mat')
print(matlab_file_contents)
