# import pandas
import pandas as pd

# define data
data = {"Name": ["Mukul", "Suraj", "Rohit",
				"Rahul", "Mohit", "Nishu",
				"Rishi", "Manoj", "Mukesh",
				"Rohan"],
		"Age": [22, 23, 25, 21, 27, 24, 26,
				23, 21, 27],
		"Qualification": ["BBA", "BCA", "BBA",
						"BBA", "MBA", "BCA",
						"MBA", "BBA", "BCA",
						"MBA"]
		}

# define dataframe
df = pd.DataFrame(data, columns=['Name', 'Age', 'Qualification'])

# display original dataframe
print("\n Original Dataframe \n", df)

# filter 5 index value
df_1 = df.filter(items=[5], axis=0)

# display result
print("\n Display only 5 index value \n", df_1)

# filter only 5 and 8 index value
df_2 = df.filter(items=[5, 8], axis=0)

# display result
print("\n Display only 5 and 8 index value \n", df_2)
