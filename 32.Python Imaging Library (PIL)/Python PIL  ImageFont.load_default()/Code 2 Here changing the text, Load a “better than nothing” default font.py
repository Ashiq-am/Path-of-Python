

from PIL import Image, ImageFont, ImageDraw

text = "better than nothing"
font = ImageFont.load_default()
im = Image.new("L", font.getsize(text), 255)

# document
dctx = ImageDraw.Draw(im)
dctx.text((0, 0), text, font = font)
del dctx
im = im.resize((im.width * 6, im.height * 6))

# img is saved as specified
im.save("geeks2.png")
