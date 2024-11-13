# image watermark
size = (500, 100)
crop_image = image.copy()
crop_image.thumbnail(size)

# add watermark
copied_image = image.copy()
copied_image.paste(crop_image, (500, 200))
plt.imshow(copied_image)
