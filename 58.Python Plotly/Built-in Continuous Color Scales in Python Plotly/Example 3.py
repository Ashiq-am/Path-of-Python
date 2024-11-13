# import packages and libraries
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import plotly.express as px

# reading the dataset
df = pd.read_csv('weather.csv', encoding='UTF-8')

# plot a scatterplot
fig = px.scatter(df, x="Temperature", y='Humidity', color='Light',
				title="Numeric 'size' values represents continuous color")


fig.show()
