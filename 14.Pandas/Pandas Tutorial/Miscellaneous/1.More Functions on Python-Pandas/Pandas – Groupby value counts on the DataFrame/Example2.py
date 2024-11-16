# import pandas
import pandas as pd

# create dataframe
df = pd.DataFrame({
	'City': ['Saharanpur', 'Meerut', 'Saharanpur', 'Saharanpur', 'Meerut'],
	'Employes Name': ['Robin', 'Tushar', 'Rohan', 'Mukul', 'Manoj'],
	'Salary': [21000, 22000, 21000, 22000, 22000]})


# print original dataframe
print("original dataframe: ")
display(df)

# counts Groupby value
df = df.groupby(['City', 'Employes Name', 'Salary']
				).size().unstack(fill_value=0)

# print dataframe
print("result: ")
display(df)
