#importing pandas as pd
import pandas as pd

# Create the dataframe
df = pd.DataFrame({
'Cust_No': [1,2,3],
'Cust_Name': ['Alex', 'Bob', 'Sophie'],
'Product_id': [12458,48484,11311],
'Product_cost': [65.25, 25.95, 100.99],
'Purchase_Date': [pd.Timestamp('20180917'),
				pd.Timestamp('20190910'),
				pd.Timestamp('20200610')]
})

# Print the dataframe
df
