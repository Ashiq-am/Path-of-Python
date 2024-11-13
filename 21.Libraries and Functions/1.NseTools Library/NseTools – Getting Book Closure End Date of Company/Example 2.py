# importing nse from nse tools
from nsetools import Nse

# creating a Nse object
nse = Nse()

# nse stock code for sbi
code = "sbin"

# getting stock quote
quote = nse.get_quote(code)

# getting book closure end date
value = quote['bcEndDate']

# printing book closure end date
print("Book closure end date : " + str(value))
