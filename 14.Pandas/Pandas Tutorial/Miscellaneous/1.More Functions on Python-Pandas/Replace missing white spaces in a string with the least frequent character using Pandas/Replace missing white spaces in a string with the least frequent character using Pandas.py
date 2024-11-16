# importing pandas library
import pandas as pd

# taking string with white spaces
newstr1 = 'akash loves gfg'

# printing the original string
print("Original String given by user:", newstr1)

# converting string into
# list of charcaters
ser = pd.Series(list(newstr1))

# counting the frequency
# of characters
element_freq = ser.value_counts()

# printing character and their
# respective frequency
print(element_freq)

current_freq = element_freq.dropna().index[-1]

# function element_freq.dropna()
# will Return a new Series with
# missing values removed
result = "".join(ser.replace(' ', current_freq))

print(result)
