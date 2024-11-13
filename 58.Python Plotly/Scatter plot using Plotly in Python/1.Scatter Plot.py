import plotly.express as px
import numpy as np

# creating random data through randomint
# function of numpy.random
np.random.seed(42)

random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

plot = px.scatter(random_x, random_y)
plot.show()
