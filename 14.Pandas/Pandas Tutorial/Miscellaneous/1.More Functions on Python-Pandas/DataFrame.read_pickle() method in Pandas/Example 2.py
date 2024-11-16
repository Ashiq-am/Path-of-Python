# importing packages
import pandas as pd

# dictionary of data
dct = {"f1": range(6), "b1": range(6, 12)}

# forming dataframe
data = pd.DataFrame(dct)

# using to_pickle function to form file
# with name 'pickle_data'
pd.to_pickle(data,'./pickle_data.pkl')

# unpickled the data by using the
# pd.read_pickle method
unpickled_data = pd.read_pickle("./pickle_data.pkl")
print(unpickled_data)
