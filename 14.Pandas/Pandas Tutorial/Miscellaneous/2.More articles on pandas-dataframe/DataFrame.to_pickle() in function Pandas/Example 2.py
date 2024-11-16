# importing packages
import pandas as pd

# dictionary of data
dct = {"f1": range(6), "b1": range(6, 12)}

# forming dataframe and printing
data = pd.DataFrame(dct)
print(data)

# using to_pickle function to form
# file with name 'pickle_file'
data.to_pickle('pickle_file')
