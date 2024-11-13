# storing image path
fname = r'g4g.png'

# opening image using pil
image = Image.open(fname).convert("L")

# maping image to gray scale
plt.imshow(image, cmap='gray')
plt.show()
