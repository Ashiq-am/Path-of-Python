import scipy.io as syio

# Save the mat file
string = 'Geeks for geeks!'
syio.savemat('str.mat', {'str': string})

# Load the mat File
matlab_file_contents = syio.loadmat('str.mat')
print(matlab_file_contents)

# printing the contents of mat file.
matlab_file_contents = syio.whosmat('str.mat')
print(matlab_file_contents)
