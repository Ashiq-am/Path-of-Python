# Importing re package for using regular expressions
import re


# Function to clean the names
def Clean_names(City_name):
    # Search for opening bracket in the name followed by
    # any characters repeated any number of times
    if re.search('\(.*', City_name):

        # Extract the position of beginning of pattern
        pos = re.search('\(.*', City_name).start()

        # return the cleaned name
        return City_name[:pos]

    else:
        # if clean up needed return the same name
        return City_name

    # Updated the city columns


df['City'] = df['City'].apply(Clean_names)

# Print the updated dataframe
print(df)
