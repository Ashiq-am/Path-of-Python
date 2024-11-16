# Pandas is imported in order to use various inbuilt
# Functions available in Pandas framework
import pandas as pd

# Data is initialized here
data = [["Jagroop", "Male"], ["Parveen", "Male"],
		["Harjot", "Female"], ["Pooja", "Female"],
		["Mohit", "Male"]]

# Data frame is created under column name Name and Gender
data_frame = pd.DataFrame(data, columns=["Name", "Gender"])

# Data of Gender is converted into Binary Data
df_one = pd.get_dummies(data_frame["Gender"])

# Binary Data is Concatenated into Dataframe
df_two = pd.concat((df_one, data_frame), axis=1)

# Gendercolumn is droped
df_two = df_two.drop(["Gender"], axis=1)

# We want Male =0 and Female =1 So we drop Male colunm here
df_two = df_two.drop(["Male"], axis=1)

# Rename the Column
result = df_two.rename(columns={"Female": "Gender"})

# Print the Result
print(result)
