# importing packages
import pandas as pd

# dictionary of data
dct = {"C1": range(5), "C2": range(5, 10)}

# forming dataframe and printing
data = pd.DataFrame(dct)
print(data)

# using to_pickle function to form file
# we can also select compression type
# file will be created in the given path
data.to_pickle('file.gzip')
