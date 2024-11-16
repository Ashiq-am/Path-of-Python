# Import the required library
import pandas

# Copy file contents which are in proper format
# Whatever data you have copied will
# get transferred to dataframe object
# Method does not accept any parameter
pdCopiedData = pd.read_clipboard()

# Print the data frame object
print(pdCopiedData)
