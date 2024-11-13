import yfinance as yahooFinance


GetFacebookInformation = yahooFinance.Ticker("FB")

# display Company Sector
print("Company Sector : ", GetFacebookInformation.info['sector'])

# display Price Earnings Ratio
print("Price Earnings Ratio : ", GetFacebookInformation.info['trailingPE'])

# display Company Beta
print(" Company Beta : ", GetFacebookInformation.info['beta'])
