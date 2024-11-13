# import packages and libraries
import pandas as pd
import plotly.express as px

# reading the dataset
df = pd.read_csv('weather.csv', encoding='UTF-8')

# plot a scatterplot
fig = px.scatter(df, x="Temperature", y='Humidity', color='Light',
				title="setting up colour palette",
				color_continuous_scale=["orange", "red",
										"green", "blue",
										"purple"])


fig.show()
