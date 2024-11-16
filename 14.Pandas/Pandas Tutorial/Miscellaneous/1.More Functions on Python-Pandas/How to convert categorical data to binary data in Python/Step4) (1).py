# import required modules
import pandas as pd

# assign data
data = [["Jagroop", "Male"], ["Praveen", "Male"],
		["Harjot", "Female"], ["Pooja", "Female"],
		["Mohit", "Male"]]

# display categorical output
data_frame = pd.DataFrame(data, columns=["Name", "Gender"])
# print(data_frame)

# converting to binary data
df_one = pd.get_dummies(data_frame["Gender"])
# print(df_one)

# display result
df_two = pd.concat((df_one, data_frame), axis=1)
df_two = df_two.drop(["Gender"], axis=1)
df_two = df_two.drop(["Male"], axis=1)
result = df_two.rename(columns={"Female": "Gender"})
print(result)
