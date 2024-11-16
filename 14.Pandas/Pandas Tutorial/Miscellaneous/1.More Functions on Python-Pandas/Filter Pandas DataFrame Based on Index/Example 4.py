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
				'Person_A', 'Person_B', 'Person_AB', 'Person_C', 'Person_BC'])

# display original dataframe
print("\n Original Dataframe \n", df)

# filter index that contain an specific character.
df_1 = df.filter(like='B', axis=0)

# display result
print("\n display all indexes that contain Specific chatacter \n", df_1)
