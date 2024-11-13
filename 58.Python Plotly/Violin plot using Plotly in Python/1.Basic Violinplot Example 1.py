import plotly.express as pt
import pandas as pd

data = pd.read_csv("C:\\Users\\Vanshi\\Desktop\\gfg\\bestsellers.csv")
df = pd.DataFrame(data)
data = df.head()

fig = pt.violin(data, y="Year")
fig.show()
