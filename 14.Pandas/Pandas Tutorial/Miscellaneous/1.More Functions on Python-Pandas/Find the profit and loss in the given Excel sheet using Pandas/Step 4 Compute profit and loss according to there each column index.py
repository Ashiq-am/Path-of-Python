# Loop for accessing every index in DataFrame
# and compute Profit and loss
# and store into new column in DataFrame
for row in range(0, len(data)):
	if data.iat[row, index_selling] > data.iat[row, index_cost]:
		data.iat[row, index_profit] = data.iat[row,
											index_selling] - data.iat[row, index_cost]
	else:
		data.iat[row, index_loss] = data.iat[row, index_cost]-data.iat[row, index_selling]
data
