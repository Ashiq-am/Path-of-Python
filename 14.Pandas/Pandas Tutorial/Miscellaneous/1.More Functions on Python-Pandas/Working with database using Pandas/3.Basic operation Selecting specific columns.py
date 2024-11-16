# read the data from sql to
# pandas dataframe.
data = pd.read_sql_query('Select * from Diabetes;', con)

# selecting specific columns.
df2 = data.loc[:, ['Glucose', 'BloodPressure']].head()
df2
