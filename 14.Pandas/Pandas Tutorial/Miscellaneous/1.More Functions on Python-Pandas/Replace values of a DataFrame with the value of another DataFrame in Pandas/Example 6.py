import pandas as pd

# Creating dataframe
df1 = pd.DataFrame([["rumul", 10, 12, 10],
					["rahul", 10, 11, 16],
					["purvi", 18, 14, 10],
					["ravi", 20, 13, 30]],
				columns=["Name1", "Maths",
							"Physics",
							"Chemistry"])

# setting name1 as index column
df1 = df1.set_index('Name1')

display(df1)

# Creating another dataframe for
# replacement
df2 = pd.DataFrame(
[["rahul", 1, 1]],
columns=["Name2", "Maths", "Physics"])

df3 = pd.DataFrame(
[["purvi", 5, 8]],
columns=["Name3", "Maths", "Chemistry"])

# setting name2 and name3 as
# index column
df2 = df2.set_index('Name2')
df3 = df3.set_index('Name3')

# update the values at the
# passed index
df1.update(df2)
df1.update(df3)

display(df1)
