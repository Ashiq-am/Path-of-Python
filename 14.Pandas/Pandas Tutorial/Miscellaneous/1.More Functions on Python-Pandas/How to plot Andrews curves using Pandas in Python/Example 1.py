# importing various package
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# making data frame from csv file
df = pd.read_csv('C:\\Users\\digital india\\Desktop\\pand.csv')

# Creating Andrews curves
x = pd.plotting.andrews_curves(df, 'animal')

# ploting the Curve
x.plot()

# Display
plt.show()
