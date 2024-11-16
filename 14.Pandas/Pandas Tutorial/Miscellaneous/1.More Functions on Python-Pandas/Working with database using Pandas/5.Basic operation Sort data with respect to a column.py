# read the data from sql
# to pandas dataframe.
data = pd.read_sql_query('Select * from Diabetes;', con)

# sort data with respect
# to particular column.
data.sort_values(by ='Age').head()
