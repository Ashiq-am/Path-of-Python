# importing nse from nse tools
from nsetools import Nse

# creating a Nse object
nse = Nse()

# nse stock code for sbi
code = "sbin"

# getting stock quote
quote = nse.get_quote(code)

# getting book closure start date
value = quote['bcStartDate']

# printing book closure start date
print("Book closure Start date : " + str(value))
