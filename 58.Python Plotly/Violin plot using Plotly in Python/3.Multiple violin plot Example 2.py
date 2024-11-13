import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv("C:\\Users\\Vanshi\\Desktop\\gfg\\bestsellers.csv")
df = pd.DataFrame(data)

plot = go.Figure(data=go.Violin(x=df['Year'], y=df['Price']))
plot.show()
