# import the pandas lib as pd
import pandas as pd

# create a dictionary
dictionary = {'A' : 50, 'B' : 10, 'C' : 80}

# create a series
series = pd.Series(dictionary, index =['B', 'C', 'D', 'A'])

print(series)
