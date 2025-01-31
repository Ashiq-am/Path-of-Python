# import libraries
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# define dimensions
width = 0.8
height = 0.25
minValue = 1
maxValue = 20

# Create dimentions of slider
dimentions_of_slider = plt.axes([0, 0, width, height])

# Create slider
# Notice the HEX color code below
mySlider = Slider(dimentions_of_slider, 'My Slider',
				minValue, maxValue, valinit=10,
				color='#000000')

# Show Graph
plt.show()
