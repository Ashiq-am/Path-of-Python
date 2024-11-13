import plotly.express as px
import pandas as pd

data = pd.read_csv("C:\\Users\\Vanshi\\Desktop\\gfg\\bestsellers.csv")
df = pd.DataFrame(data)

plot = px.violin(df, x=df['Year'], y=df['Price'], color=df['Genre'])
plot.show()
