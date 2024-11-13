''''''
import Slider as Slider
from self import self

"""To add some styling and coloring to the slider, just replace the line no 42 with the below and add 
some new features also if you want. 
For text, styling uses the proper commands in text portion."""



# declaring the slider and adding some effects to it
# By default its orientation is horizontal
# if want to change to vertical do like below
self.brightnessControl = Slider(min = 0, max = 100,
								orientation ='vertical',
								value_track = True,
								value_track_color =[1, 0, 0, 1])
