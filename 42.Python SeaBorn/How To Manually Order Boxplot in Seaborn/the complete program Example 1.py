# import required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# load dataset
tips= sns.load_dataset('tips')


# display top most rows
tips.head()


# illustraing box plot with order
sns.boxplot(x='day', y='total_bill', data=tips, order=[
				'Sun', 'Sat', 'Fri', 'Thur'], hue='sex', palette='Set2')
