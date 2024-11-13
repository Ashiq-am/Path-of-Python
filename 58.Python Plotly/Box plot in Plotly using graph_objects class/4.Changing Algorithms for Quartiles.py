import plotly.graph_objects as px
import numpy as np


# creating random data through randomint
# function of numpy.random
np.random.seed(42)

random_y= np.random.randint(1,101,100)

x = ['A', 'B', 'C', 'D']

plot = px.Figure()

plot.add_trace(px.Box(y=random_y, quartilemethod="linear", name="linear"))
plot.add_trace(px.Box(y=random_y, quartilemethod="inclusive", name="inclusive"))
plot.add_trace(px.Box(y=random_y, quartilemethod="exclusive", name="exclusive"))

plot.show()
