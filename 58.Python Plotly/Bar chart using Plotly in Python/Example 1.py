import plotly.express as px
import numpy

# creating random data through randomint
# function of numpy.random
np.random.seed(42)

random_x= np.random.randint(1, 101, 100)
random_y= np.random.randint(1, 101, 100)

fig = px.bar(random_x, y = random_y)
fig.show()
