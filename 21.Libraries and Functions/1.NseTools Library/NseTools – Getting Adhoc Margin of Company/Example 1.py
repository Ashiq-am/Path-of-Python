# importing nse from nse tools
from nsetools import Nse

# creating a Nse object
nse = Nse()

# nse stock code for wipro
code = "wipro"

# getting stock quote
quote = nse.get_quote(code)

# getting adhoc margin
value = quote['adhocMargin']

# printing adhoc margin
print("Adhoc Margin : " + str(value))
