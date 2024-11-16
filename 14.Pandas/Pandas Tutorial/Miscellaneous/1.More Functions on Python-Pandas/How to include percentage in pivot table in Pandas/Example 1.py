# importing pandas library
import pandas as pd

# creating dataframe
df = pd.DataFrame({'Name': ['John', 'Sammy', 'Stephan', 'Joe', 'Emily', 'Tom'],
				'Gender': ['Male', 'Female', 'Male',
							'Female', 'Female', 'Male'],
				'Age': [45, 6, 4, 36, 12, 43]})
print("Dataset")
print(df)
print("-"*40)

# categorizing in age groups
def age_bucket(age):
	if age <= 18:
		return "<18"
	else:
		return ">18"

df['Age Group'] = df['Age'].apply(age_bucket)

# calculating gender percentage
gender = pd.DataFrame(df.Gender.value_counts(normalize=True)*100).reset_index()
gender.columns = ['Gender', '%Gender']
df = pd.merge(left=df, right=gender, how='inner', on=['Gender'])

# creating pivot table
table = pd.pivot_table(df, index=['Gender', '%Gender', 'Age Group'],
					values=['Name'], aggfunc={'Name': 'count',})

# display table
print("Table")
print(table)
