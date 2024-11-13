import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv("C:\\Users\\Vanshi\\Desktop\\gfg\\bestsellers.csv")
df = pd.DataFrame(data)

plot = go.Figure(data=go.Violin(
	y=df['Price'], points='all', pointpos=2, box_visible=True))

plot.show()
