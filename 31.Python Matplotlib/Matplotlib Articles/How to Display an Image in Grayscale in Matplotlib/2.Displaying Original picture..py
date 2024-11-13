# storing image path
fname = r'g4g.png'

# opening image using pil
image = Image.open(fname)

# plottingimage
plt.imshow(image)
plt.show()
