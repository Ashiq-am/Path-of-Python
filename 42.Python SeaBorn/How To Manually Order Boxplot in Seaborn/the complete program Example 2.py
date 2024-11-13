# import required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# load dataset
tips = sns.load_dataset('tips')


# display top most rows
tips.head()


# plotting the boxplot taking time on x-axis
fx = sns.boxplot(x="time", y="total_bill", hue="smoker",
				data=tips, palette="Set1")

# illustrating box plot with order
ax = sns.boxplot(x="time", y="total_bill", hue="smoker", order=['Dinner', 'Lunch'],
				data=tips, palette="Set1")
