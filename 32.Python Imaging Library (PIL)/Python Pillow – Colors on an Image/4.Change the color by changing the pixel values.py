from PIL import Image

img = Image.open("flower.jpg")
img = img.convert("RGB")

d = img.getdata()

new_image = []
for item in d:

    # change all white (also shades of whites)
    # pixels to yellow
    if item[0] in list(range(200, 256)):
        new_image.append((255, 224, 100))
    else:
        new_image.append(item)

# update image data
img.putdata(new_image_data)

# save new image
img.save("flower_image_altered.jpg")
