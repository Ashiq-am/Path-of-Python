# Set index for each column
index_selling=df.columns.get_loc('Selling Price')
index_cost=df.columns.get_loc('Cost price')
index_total=df.columns.get_loc('Total')
index_max=df.columns.get_loc('Maximum')

print(index_selling,index_cost,index_total,index_max)
