import pandas as pd
import plotly.express as px

d = {'col1': [1, 2, 3], 'col2': [3, 4, 5]}
df = pd.DataFrame(data=d)

fig = px.line(df, x=df.index, y=['col1', 'col2'])

fig.update_traces({'name': 'hello'}, selector={'name': 'col1'})
fig.update_traces({'name': 'hi'}, selector={'name': 'col2'})

fig.show()
