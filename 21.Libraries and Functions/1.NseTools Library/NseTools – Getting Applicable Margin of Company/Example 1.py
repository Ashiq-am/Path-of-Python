# importing nse from nse tools
from nsetools import Nse

# creating a Nse object
nse = Nse()

# nse stock code for wipro
code = "wipro"

# getting stock quote
quote = nse.get_quote(code)

# getting applicable margin
value = quote['applicableMargin']

# printing applicable margin
print("Applicable Margin : " + str(value))
