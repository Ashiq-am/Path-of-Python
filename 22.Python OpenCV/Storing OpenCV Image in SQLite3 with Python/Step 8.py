# Use pandas to create a dataframe from
# the table and save it as a csv
table = pd.read_sql_query("SELECT * FROM imgfg", conn)
table.to_csv("imgfg" + '.csv', index_label='index')
