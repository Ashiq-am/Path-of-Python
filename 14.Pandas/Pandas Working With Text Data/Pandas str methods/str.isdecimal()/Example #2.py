''''''
'''In this example, numbers with power are also added to that column. Both str isdigit() and 
str.isdecimal() are called and output is stored in different columns to compare the difference between 
both.'''


# importing pandas module
import pandas as pd

# creating data frame
data = pd.DataFrame(["hey", "gfg", 3, "4²", 5, "5.5", "129²"])

# calling method and returning series
data["Bool"]= data[0].str.isdecimal()

# calling method and returning series
data["Bool2"]= data[0].str.isdigit()

# display
data
