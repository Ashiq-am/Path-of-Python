import pandas as pd

# Sample data with URLs
data = {
       "Description": ["GeeksForGeeks", "Python Documentation", "Pandas Documentation"],
       "URL": [
           "https://www.geeksforgeeks.org/",
           "https://docs.python.org/3/",
           "https://pandas.pydata.org/docs/"
       ]
   }

# Create DataFrame
df = pd.DataFrame(data)
