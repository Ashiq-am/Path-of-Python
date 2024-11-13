import yfinance as yf

# Define the ticker symbol
ticker = 'AAPL'

# Get the ticker object
stock = yf.Ticker(ticker)

# Get the balance sheet
balance_sheet = stock.balance_sheet
print("Balance Sheet:")
print(balance_sheet.head())

# Get the income statement
income_statement = stock.financials
print("\nIncome Statement:")
print(income_statement.head())
