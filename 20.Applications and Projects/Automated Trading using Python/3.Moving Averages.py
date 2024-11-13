# assigning adjusted closing prices
# to adj_prices
adj_price = msft_data['Adj_Close']

# calculate the moving average
mav = adj_price.rolling(window=50).mean()

# print the result
print(mav[-10:])
