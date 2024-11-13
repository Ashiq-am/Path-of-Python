# text Watermark
from PIL import ImageFont
from PIL import ImageDraw
watermark_image = image.copy()

draw = ImageDraw.Draw(watermark_image)
font = ImageFont.truetype("arial.ttf", 50)

# add watermark
draw.text((0, 0), "puppy",
		(0, 0, 0), font=font)
plt.subplot(1, 2, 1)
plt.title("black text")
plt.imshow(watermark_image)

# add watermark
draw.text((0, 0), "puppy",
		(255, 255, 255), font=font)
plt.subplot(1, 2, 2)
plt.title("white text")
plt.imshow(watermark_image)
