# Aligning index
aapl["MSFT"] = msft.MSFT

# removing Missing Values
aapl.dropna(inplace=True)

aapl.head(10)
