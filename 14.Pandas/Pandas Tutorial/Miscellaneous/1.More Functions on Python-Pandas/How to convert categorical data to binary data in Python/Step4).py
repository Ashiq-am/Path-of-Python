# import required modules
import pandas as pd

# assign data
data = [["Jagroop", "Male"], ["Praveen", "Male"],
		["Harjot", "Female"], ["Pooja", "Female"],
		["Mohit", "Male"]]

# display categorical output
data_frame = pd.DataFrame(data, columns=["Name", "Gender"])
print(data_frame)

# converting to binary data
df_one = pd.get_dummies(data_frame["Gender"])
print(df_one)
