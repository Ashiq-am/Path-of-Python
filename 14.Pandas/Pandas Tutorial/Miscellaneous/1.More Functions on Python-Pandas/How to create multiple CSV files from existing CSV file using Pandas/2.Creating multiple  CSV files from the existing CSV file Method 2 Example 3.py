import pandas as pd

# read DataFrame
data = pd.read_csv("Customers.csv")

male = data[data['Gender'] == 'Male']
female = data[data['Gender'] == 'Female']

male.to_csv('Gender_male.csv', index=False)
female.to_csv('Gender_female.csv', index=False)

print(pd.read_csv("Gender_male.csv"))
print(pd.read_csv("Gender_female.csv"))
