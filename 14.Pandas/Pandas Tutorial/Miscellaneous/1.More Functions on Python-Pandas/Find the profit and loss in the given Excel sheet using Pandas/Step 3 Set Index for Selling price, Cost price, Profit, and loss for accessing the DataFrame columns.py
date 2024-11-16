# set index
index_selling = data.columns.get_loc('Selling Price')
index_cost = data.columns.get_loc('Cost price')
index_profit = data.columns.get_loc('Profit')
index_loss = data.columns.get_loc('Loss')

print(index_selling, index_cost, index_profit, index_loss)
