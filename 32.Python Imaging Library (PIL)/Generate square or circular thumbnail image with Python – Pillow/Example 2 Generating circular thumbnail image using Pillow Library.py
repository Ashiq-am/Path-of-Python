# importing necessary libraries
from PIL import Image, ImageDraw
import numpy as np

# opening the image from
# the storage using Image.open() function
orig_img=Image.open('sebastian-molina.jpg')

# getting height and width of
# an image using size() function
height,width=orig_img.size

# converting image to numpy array
npImage=np.array(orig_img)

# Creating mask image in L mode with same image size
new_img = Image.new('L', orig_img.size,0)

# drawing on mask created image using Draw() function
draw = ImageDraw.Draw(new_img)

# making circle on mask image using pieslice() function
draw.pieslice([0,0,height,width],0,360,fill=255)

# Converting the mask Image to numpy array
np_new=np.array(new_img)

# stack the array sequence
# (original image array with mask image) depth wise
npImage=np.dstack((npImage,np_new))

# converting array to an image using fromarray() function
final_img = Image.fromarray(npImage)

# making thumbnail using thumbnail()
# function by passing the size in it
final_img.thumbnail((500,500))

# saving the circular thumbnail Image
final_img.save('Circular_thumbnail.png')
