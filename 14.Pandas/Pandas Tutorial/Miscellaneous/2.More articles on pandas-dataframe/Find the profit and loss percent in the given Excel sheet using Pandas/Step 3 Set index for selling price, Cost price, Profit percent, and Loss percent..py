# set index
index_selling = data.columns.get_loc('Selling Price')
index_cost = data.columns.get_loc('Cost price')
index_profit = data.columns.get_loc('Profit percent')
index_loss = data.columns.get_loc('Loss percent')

print(index_selling, index_cost, index_profit, index_loss)
