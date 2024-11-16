import numpy as np
# take random data

# random.choice(x,y) will pick y elements from range (0,(x-1))
data = np.random.choice(10, 20)

# specify the dimensons of data i.e (rows,columns)
data = data.reshape(5, 4)

# print original data having rows with all zeroes
print("Original Dataset")
print(data)

# make some rows entirely zero
data[1, :] = 0 # making 2nd row entirely 0
data[4, :] = 0 # making last row entirely 0

# after making 2nd and 5th row as 0
print("After making some rows as entirely 0")
print(data)
data = data[~np.all(data == 0, axis=1)]

# data after removing rows having all zeroes
print("After removing rows")
print(data)
