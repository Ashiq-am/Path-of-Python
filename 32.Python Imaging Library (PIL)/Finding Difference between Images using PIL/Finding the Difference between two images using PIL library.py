from PIL import Image, ImageChops


img1 = Image.open('p.jpg')
img2 = Image.open('r.jpg')

diff = ImageChops.difference(img1, img2)

if diff.getbbox():
	diff.show()
