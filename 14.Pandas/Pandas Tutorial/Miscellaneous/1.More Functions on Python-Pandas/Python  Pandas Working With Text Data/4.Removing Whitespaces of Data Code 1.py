# importing pandas module
import pandas as pd

# Define a dictionary containing employee data
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age': [27, 24, 22, 32],
        'Address': ['Nagpur junction', 'Kanpur junction',
                    'Nagpur junction', 'Kannuaj junction'],
        'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame
df = pd.DataFrame(data)

# replacing address name and adding spaces in start and end
new = df["Address"].replace("Nagpur junction", "  Nagpur junction  ").copy()

# checking with custom string
print(new.str.strip() == " Nagpur junction")
print(new.str.strip() == "Nagpur junction ")
print(new.str.strip() == " Nagpur junction ")
