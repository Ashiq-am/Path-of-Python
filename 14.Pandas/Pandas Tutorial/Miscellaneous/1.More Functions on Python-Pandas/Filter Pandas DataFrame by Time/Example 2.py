import pandas as pd

# create data frame
Data = {'Name': ['Mukul', 'Rohan', 'Mayank',
						'Shubham', 'Aakash'],

		'DOB': ['1997-04-24', '1998-05-25', '1999-04-11',
				'2000-11-15', '1998-06-28']}
df = pd.DataFrame(Data)

# print original data frame
print(df)

Date1 = df["DOB"] >= "1998-04-24"
Date2 = df["DOB"] <= "1999-1-31"

# filter data between 1998-04-24 to 1999-01-31
New_df = df.loc[Date1 & Date2]

# print the filtered data frame
print(New_df)
