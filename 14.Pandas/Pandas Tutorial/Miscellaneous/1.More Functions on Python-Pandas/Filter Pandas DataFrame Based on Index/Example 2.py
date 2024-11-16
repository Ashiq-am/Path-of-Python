# import pandas
import pandas as pd

# define data
data = {"Name": ["Mukul", "Suraj", "Rohit",
				"Rahul", "Mohit"],
		"Age": [22, 23, 25, 21, 27],
		"Qualification": ["BBA", "BCA", "BBA",
						"BBA", "MBA"]
		}

# define dataframe
df = pd.DataFrame(data, columns=['Name', 'Age', 'Qualification'], index=[
				'Person_A', 'Person_B', 'Person_C', 'Person_D', 'Person_E'])

# display original dataframe
print("\n Original Dataframe \n", df)

# filter Person_B index value
df_1 = df.filter(items=['Person_B'], axis=0)

# display result
print("\n Display only Person_B index value \n", df_1)

# filter only Person_B and Person_D index value
df_2 = df.filter(items=['Person_B', 'Person_D'], axis=0)

# display result
print("\n Display Person_B and Person_D index value \n", df_2)
