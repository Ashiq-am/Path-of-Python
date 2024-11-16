# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj', 'Geeku'],
        'Age': [27, 24, 22, 32, 15],
        'Address': ['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Noida'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd', '10th']}

# Create own index
index = {'a', 'b', 'c', 'd', 'e'}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data, index)

# set index any column of our DF and
# remove default index
df.set_index(['Age'], inplace=True)

df
