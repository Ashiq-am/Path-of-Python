from PIL import Image

img = Image.open("gfg.png")

rot_img = img.rotate(180)

rot_img.save("rotated_gfg.png")
