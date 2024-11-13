import plotly.graph_objects as px
import numpy as np


# creating random data through randomint
# function of numpy.random
np.random.seed(42)

random_x1= np.random.randint(1,101,100)
random_x2= np.random.randint(1,101,100)

x = ['A', 'B', 'C', 'D']

plot = px.Figure()

plot.add_trace(px.Box(x=random_x1, marker_color = 'indianred', boxmean=True))
plot.add_trace(px.Box(x=random_x2, marker_color='royalblue', boxmean='sd'))

plot.show()
