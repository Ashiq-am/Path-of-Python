from pandas.tests.test_downstream import df

total_goals = df['Goals'].groupby(df['Team'])

# printing the means value
print(total_goals.mean())
