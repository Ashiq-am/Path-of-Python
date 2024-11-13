# importing modules
from PIL import ImageTk, Image
from matplotlib import pyplot as plt

# depicting the visualization
testImage = Image.open('g4g.png')

# displaying the title
plt.title("Geeks 4 Geeks",
		fontsize='20',
		backgroundcolor='green',
		color='white')
plt.imshow(testImage)
