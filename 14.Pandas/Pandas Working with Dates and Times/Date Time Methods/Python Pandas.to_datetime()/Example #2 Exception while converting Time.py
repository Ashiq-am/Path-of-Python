'''

'''


'''Time object can also be converted with this method. But since in the Time column, a date 
isn’t specified and hence Pandas will put Today’s date automatically in that case.'''



# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("todatetime.csv")

# overwriting data after changing format
data["Time"]= pd.to_datetime(data["Time"])

# info of data
data.info()

# display
data
