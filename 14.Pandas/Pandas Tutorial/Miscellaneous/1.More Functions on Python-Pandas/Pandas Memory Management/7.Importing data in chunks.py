# importing the mmodule
import pandas

# Reading the data in chunks
data = pandas.read_csv('data.csv', chunksize=1000)

# Concatenating the chunks together
df = pandas.concat(data)
