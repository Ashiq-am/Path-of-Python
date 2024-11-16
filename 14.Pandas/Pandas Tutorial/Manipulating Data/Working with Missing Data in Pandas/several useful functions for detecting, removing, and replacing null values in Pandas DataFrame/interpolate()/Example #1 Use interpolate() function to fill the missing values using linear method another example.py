''''''
'''Let’s interpolate the missing values using Linear method. Note that Linear method ignore the 
index and treat the values as equally spaced.'''




from pandas.tests.groupby.test_value_counts import df

# to interpolate the missing values
df.interpolate(method ='linear', limit_direction ='forward')
