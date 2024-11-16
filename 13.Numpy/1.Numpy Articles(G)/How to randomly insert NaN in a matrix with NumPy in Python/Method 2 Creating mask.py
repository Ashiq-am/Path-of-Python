import numpy as np

# creating dataset
X = 10
Y = 5
N = 15

data = np.random.randn(X, Y)

# making a array randomly of same size as data of bool type
mask = np.zeros(X*Y, dtype=bool)

# marking first n indexes as true
mask[:N] = True

# shuffling the maks
np.random.shuffle(mask)
mask = mask.reshape(X, Y)

# applying mask to the data
data[mask] = np.nan
print(data)
