# importing pandas module
import pandas as pd

# creating series 2
series2 = pd.Series([1, 2, 3, 10, 2])

# try except for series2
# since series 2 is a numeric series
try:
    result2 = series2.str.isspace()
    print('Series 2 results: \n\n', result2)

except Exception as e:

    # printing error in
    print('\nError occured - {}'.format(e))

    # new result by first converting to string series
    # using .astype()
    result2 = series2.astype(str).str.isspace()

    # printing results
    print('\nSeries 2 results: \n\n', result2)
