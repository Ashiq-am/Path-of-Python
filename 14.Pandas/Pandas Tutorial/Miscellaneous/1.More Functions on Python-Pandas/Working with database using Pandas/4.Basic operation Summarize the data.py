# read the data from sql
# to pandas dataframe.
data = pd.read_sql_query('Select * from Diabetes;', con)

# summarize the data
data.describe()
