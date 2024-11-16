import pandas as pd

# create data frame
Data = {'Name': ['Mukul', 'Rohan', 'Mayank',
						'Shubham', 'Aakash'],

		'DOB': ['1997-04-24', '1998-05-25', '1999-04-11',
				'2000-11-15', '1998-06-28']}

df = pd.DataFrame(Data)

# print original data frame
print(df)

# filter data frame
New_df = df.loc[df["DOB"] >= "1999-02-5"]

# print filtered data frame
print(New_df)
