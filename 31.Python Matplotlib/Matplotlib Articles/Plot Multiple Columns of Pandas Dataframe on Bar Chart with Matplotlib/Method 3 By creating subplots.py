# importing pandas library
import pandas as pd
# import matplotlib library
import matplotlib.pyplot as plt

# creating dataframe
df = pd.DataFrame({
	'Name': ['John', 'Sammy', 'Joe'],
	'Age': [45, 38, 90],
	'Height(in cm)': [150, 180, 160]
})

# creating subplots and plotting them together
ax = plt.subplot()
ax.bar(df["Name"], df["Height(in cm)"])
ax.bar(df["Name"], df["Age"], color="maroon")
