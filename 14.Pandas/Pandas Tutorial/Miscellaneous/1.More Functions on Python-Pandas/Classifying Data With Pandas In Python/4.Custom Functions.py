# Sample DataFrame
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
				'Age': [22, 18, 25]})

# Custom function for age classification
def classify_age(age):
	if age < 20:
		return 'Young'
	elif 20 <= age <= 25:
		return 'Mid-age'
	else:
		return 'Senior'

# Apply the custom function to create a new 'Age Category' column
df['Age Category'] = df['Age'].apply(classify_age)

print(df)
