import pandas as pd
data = {
	'Name': ['Disha', 'Shravan', 'Jeetu', 'Ram'],
	'Age': [21, 23, 24, 22],
	'Gender': ['Female', 'Male', 'Male', 'Male'],
	'Education': ['Graduation','Masters','Masters','Graduation'],
	'Salary':[22000,35000,35000,22000]
}
df = pd.DataFrame(data)
df
