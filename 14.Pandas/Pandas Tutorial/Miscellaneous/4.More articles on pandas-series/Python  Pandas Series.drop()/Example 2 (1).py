# drop the passed labels
result = sr.drop(labels = [pd.Timestamp('2010-12-31'),
						pd.Timestamp('2011-04-30'), pd.Timestamp('2011-08-31')])

# Print the result
print(result)
