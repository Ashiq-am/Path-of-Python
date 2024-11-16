# using [] method
print("Selecting Single column value using dataframe[column name]")
series_one = pd.Series(df['Age'])
print(series_one)

print("Type of selected one")
print(type(series_one))
