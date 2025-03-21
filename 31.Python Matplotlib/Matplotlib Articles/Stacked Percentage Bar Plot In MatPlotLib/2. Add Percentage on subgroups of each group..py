# importing packages
import pandas as pd
import numpy as np
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
title = 'Percentage Stacked Bar Graph',
mark_right = True)

df_total = df["Studied"] + df["Slept"] + df["Other"]
df_rel = df[df.columns[1:]].div(df_total, 0)*100

for n in df_rel:
	for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n],
										df[n], df_rel[n])):
		plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%',
				va = 'center', ha = 'center')
