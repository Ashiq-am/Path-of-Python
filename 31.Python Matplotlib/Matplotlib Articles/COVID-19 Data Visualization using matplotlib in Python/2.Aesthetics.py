import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('case_time_series.csv')

Y = data.iloc[61:,1].values
R = data.iloc[61:,3].values
D = data.iloc[61:,5].values
X = data.iloc[61:,0]

plt.figure(figsize=(25,8))

ax = plt.axes()
ax.grid(linewidth=0.4, color='#8f8f8f')

ax.set_facecolor("black")
ax.set_xlabel('\nDate',size=25,color='#4bb4f2')
ax.set_ylabel('Number of Confirmed Cases\n',
			size=25,color='#4bb4f2')

ax.plot(X,Y,
		color='#1F77B4',
		marker='o',
		linewidth=4,
		markersize=15,
		markeredgecolor='#035E9B')
