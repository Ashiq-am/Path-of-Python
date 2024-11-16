# import pandas
import pandas as pd

# create dataframe
df = pd.DataFrame({
	'Employs Name': ['Rishabh', 'Rahul', 'Suraj', 'Mukul', 'Vinit'],
	'Location': ['Saharanpur', 'Meerut', 'Saharanpur', 'Meerut', 'Saharanpur'],
	'Pay': [21000, 22000, 23000, 24000, 22000]})

# print dataframe
print("\n *** Original DataFrames ** \n")
print(df)


# create dictioneries
dicts = [{'Employs Name': 'Anuj', 'Location': 'Meerut', 'Roll No': 30000},
		{'Employs Name': 'Arun', 'Location': 'Saharanpur', 'Roll No': 32000}]

# print dictioneries
print("\n ** Dictionary ** ")
print(dicts)


# combined data
df = df.append(dicts, ignore_index=True, sort=False)

# print combined dataframe
print("\n\n ** Combined Data **\n")
print(df)
