data = pd.read_csv("daily-minimum-temperatures-in-blr.csv",
				header=0, index_col=0, parse_dates=True,
				squeeze=True)

# extracting only the temperature values
values = pd.DataFrame(data.values)

# using shift function to shift the values.
dataframe = pd.concat([values.shift(3), values.shift(2),
					values.shift(1), values], axis=1)
# naming the columns
dataframe.columns = ['t', 't+1', 't+2', 't+3']

# using corr() function to compute the correlation
result = dataframe.corr()

print(result)
