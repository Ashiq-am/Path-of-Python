# import packages
import pandas as pd

# opening a file
data = open('file1.txt')

# checking if it's a file like object
print(pd.api.types.is_file_like(data))
