#Importing Image and ImageFont, ImageDraw module from PIL package



from PIL import Image, ImageFont, ImageDraw

# creating a image object
image = Image.open(r'C:\Users\System-Pc\Desktop\flower.jpg')

draw = ImageDraw.Draw(image)

font = ImageFont.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 70)

text = 'stay healthy'

draw.text((50, 100), text, font=font)

image.show()
