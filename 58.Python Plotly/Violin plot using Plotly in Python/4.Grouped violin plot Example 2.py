import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv("C:\\Users\\Vanshi\\Desktop\\gfg\\bestsellers.csv")
df = pd.DataFrame(data)

plot = go.Figure()

plot.add_trace(go.Violin(x=df['Year'][df['Genre'] == 'Fiction'],
						y=df['Price'], line_color='red', name='Fiction'))

plot.add_trace(go.Violin(x=df['Year'][df['Genre'] == 'Non Fiction'],
						y=df['Price'], line_color='blue', name='Non-Fiction'))

plot.update_layout(violinmode='group')
plot.show()
