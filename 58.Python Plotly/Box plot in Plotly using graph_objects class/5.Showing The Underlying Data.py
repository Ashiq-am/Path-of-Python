import plotly.graph_objects as px
import numpy as np


# creating random data through randomint
# function of numpy.random
np.random.seed(42)

random_y1= np.random.randint(1,101,100)
random_y2= np.random.randint(1,101,100)

x = ['A', 'B', 'C', 'D']

plot = px.Figure()

plot.add_trace(px.Box(y=random_y1, boxpoints="all"))
plot.add_trace(px.Box(y=random_y2, boxpoints="outliers"))


plot.show()
