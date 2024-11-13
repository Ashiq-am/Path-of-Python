# importing nse from nse tools
from nsetools import Nse

# creating a Nse object
nse = Nse()

# nse stock code for sbi
code = "sbin"

# getting stock quote
quote = nse.get_quote(code)

# getting average price
value = quote['averagePrice']

# printing average price
print("Average Price : " + str(value))
