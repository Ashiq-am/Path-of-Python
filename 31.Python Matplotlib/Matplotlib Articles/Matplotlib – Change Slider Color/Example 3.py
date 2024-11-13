# import libraries
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# define dimensions
width = 0.8
height = 0.25
minValue = 1
maxValue = 20

# define sliders
dimentions_of_slider1 = plt.axes([0, 0.3, width, height])
dimentions_of_slider2 = plt.axes([0, 0, width, height])

# Using name of Color
mySlider1 = Slider(dimentions_of_slider1, 'My Slider1',
				minValue, maxValue, valinit=10,
				color='brown')

# Using HEX Code of Color
mySlider2 = Slider(dimentions_of_slider2, 'My Slider2',
				minValue, maxValue, valinit=10,
				color='#123456')

# show the plot
plt.show()
