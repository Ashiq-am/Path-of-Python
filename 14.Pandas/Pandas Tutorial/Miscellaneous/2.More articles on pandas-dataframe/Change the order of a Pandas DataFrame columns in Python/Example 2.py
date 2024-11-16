# importing the modules
import pandas as pd

# creating the DataFrame
l1 =["Amar", "Barsha", "Carlos", "Tanmay", "Misbah"]
l2 =["Alpha", "Bravo", "Charlie", "Tango", "Mike"]
l3 =[23, 25, 22, 27, 29]
l4 =[69, 54, 73, 70, 74]
df = pd.DataFrame(list(zip(l1, l2, l3, l4)))
df.columns =['Name', 'Code', 'Age', 'Weight']

# printing the original DataFrame
print("My Original DataFrame")
print(df)

# altering the DataFrame
df = df[['Name', 'Code', 'Weight', 'Age']]

# printing the altered DataFrame
print('After altering Weight and Age')
print(df)
