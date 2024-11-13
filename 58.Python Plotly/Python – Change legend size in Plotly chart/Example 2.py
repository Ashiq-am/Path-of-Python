# import packages
import plotly.express as px
import pandas as pd

# importing csv file
df = pd.read_csv("iris.csv")

# scatter plot using plotly
fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species")

# update_layout method used to modify change and size
fig.update_layout(legend=dict(title_font_family="Times New Roman",
							font=dict(size= 20)
))

fig.show()
