# import packages and libraries
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import plotly.express as px

# reading the dataset
df = pd.read_csv('weather.csv', encoding='UTF-8')

# creating a scatterplot
fig = px.scatter(df, x="Temperature", y='Humidity',
				trendline='ols', trendline_color_override='red')


fig['data'][0]['showlegend'] = True
fig['data'][0]['name'] = 'Humidity'

fig.show()
