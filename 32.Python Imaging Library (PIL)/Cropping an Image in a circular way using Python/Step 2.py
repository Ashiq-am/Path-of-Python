h,w = img.size

# creating luminous image
lum_img = Image.new('L',[h,w] ,0)
draw = ImageDraw.Draw(lum_img)
draw.pieslice([(0,0),(h,w)],0,360,fill=255)
img_arr = np.array(img)
lum_img_arr = np.array(lum_img)
display(Image.fromarray(lum_img_arr))
