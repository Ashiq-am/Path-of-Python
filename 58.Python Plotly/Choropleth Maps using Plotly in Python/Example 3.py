#import libraries
import pandas as pd
import plotly.express as px

#import data
data = pd.read_csv('2011_us_ag_exports.csv')

# create choropleth map for the data
# color will be the column to be color-coded
# locations is the column with sppatial coordinates
fig = px.choropleth(data, locations='code',
					locationmode="USA-states", color='total exports', scope="usa")

fig.show()
