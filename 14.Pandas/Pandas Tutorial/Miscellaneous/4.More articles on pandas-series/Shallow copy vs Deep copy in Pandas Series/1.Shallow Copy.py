# porgam to depict shallow copy
# in pandas series

# import module
import pandas as pd

# assign series
ser = pd.Series(['Mandy', 'Ron', 'Jacob', 'Bayek'])


# shallow copy
copyser = ser.copy(deep=False)


# comparing shallow copied series
# and original series
print('\nBefore Operation:\n', copyser == ser)

# assignmnet operation
copyser[2] = 'Geeks'


# comparing shallow copied series
# and original series
print('\nAfter Operation:\n', copyser == ser)

print('\nOriginal Dataframe after operation:\n', ser)
