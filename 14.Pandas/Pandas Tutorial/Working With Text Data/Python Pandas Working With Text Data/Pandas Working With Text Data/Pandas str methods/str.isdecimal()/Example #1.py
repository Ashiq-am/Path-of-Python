''''''
'''In this example, a new data frame is created with just one column and some values are passed to it. 
Then str.isdecimal() method is called on that column and output is returned to a new column Bool'''


# importing pandas module
import pandas as pd

# creating data frame
data = pd.DataFrame(["hey", "gfg", 3, "4", 5, "5.5"])

# calling method and returning series
data["Bool"]= data[0].str.isdecimal()

# display
data
