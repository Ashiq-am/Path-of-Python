# importing packages
import pandas as pd
import matplotlib.pyplot as plt

# load dataset
df = pd.read_excel("Hours.xlsx")

# view dataset
print(df)

# plot a Stacked Bar Chart using matplotlib
df.plot(
	x = 'Name',
	kind = 'barh',
	stacked = True,
	title = 'Stacked Bar Graph',
	mark_right = True)
