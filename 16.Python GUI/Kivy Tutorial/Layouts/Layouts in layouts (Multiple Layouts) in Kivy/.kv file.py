# Program of How to use Multiple Layouts in Single .kv file

########################################################################

# creating page Layout
< PageLayout >:

#########################################################################

# Creating Page 1

# Using BoxLayout inside PageLayout
BoxLayout:

# creating Canvas
canvas:
Color:
rgba: 216 / 255., 195 / 255., 88 / 255., 1
Rectangle:
pos: self.pos
size: self.size

# Providing orentation to the BoxLayout
orientation: 'vertical'

# Adding Lable to Page 1
Label:
size_hint_y: None
height: 1.5 * self.texture_size[1]
text: 'page 1'

# Creating Button
Button:
text: 'GFG :)'

# Adding On_press funcion
# i.e binding function to press / touch
on_press: print("This Is The First Page")

#########################################################################

# Creating Page 2

BoxLayout:
orientation: 'vertical'
canvas:
Color:
rgba: 109 / 255., 8 / 255., 57 / 255., 1
Rectangle:
pos: self.pos
size: self.size
Label:
text: 'page 2'

# This Image is directly from the websource
# By using AsyncImage you can use that
AsyncImage:
source: 'http://kivy.org / logos / kivy-logo-black-64.png'

##########################################################################

# Creating Page 3

# Using The Second Layout
# Creating GridLayout
GridLayout:

canvas:
Color:
rgba: 37 / 255., 39 / 255., 30 / 255., 1
Rectangle:
pos: self.pos
size: self.size

# Adding grids to Page 3
# It may be row or coloumn
cols: 2

# In first Grid
# Adding Lable + Image
Label:
text: 'page 3'

AsyncImage:
source: 'http://kivy.org/slides/kivyandroid-thumb.jpg'

# In Second Grid
# Adding Button + Image
Button:
text: 'Its User:):)'
on_press: print("Heloo User This is the Last Page")

AsyncImage:
source: 'http://kivy.org/slides/kivypictures-thumb.jpg'

# In third grid
# Adding Widget + Image

Widget

AsyncImage:
source: 'http://kivy.org/slides/particlepanda-thumb.jpg'
