# importing various package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# making data frame from csv file
df = pd.read_csv( 'https://raw.github.com/pandas-dev/''pandas/master/pandas/tests/io/data/csv/iris.csv')

# Creating Andrews curves
x = pd.plotting.andrews_curves(df, 'Name')

# ploting the Curve
x.plot()

# Display
plt.show()
