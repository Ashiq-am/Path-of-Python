import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np


# creating random data through randomint
# function of numpy.random
np.random.seed(42)

random_x= np.random.randint(1,101,100)
random_y= np.random.randint(1,101,100)

# create variable data which holds the data
data=[go.Scatter(x=random_x,
				y=random_y,
				mode='markers',
				marker= dict(size= 12,
							color= 'rgb(51,204,153)',
							symbol= 'pentagon',
							line= {'width':2}
							) )]

# create layout of scatter plot
layout=go.Layout(title='Random Scatter Plot',
				xaxis= {'title':'X-AXIS'} ,
				yaxis= dict(title='Y-AXIS'),
				hovermode= 'closest' )

# create figure variable to pass the
# data and Layout
fig= go.Figure(data=data , layout=layout)

# call plot function using plotly offline
pyo.plot(fig, filename='scatterplot-1.html')
