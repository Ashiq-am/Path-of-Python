# rotate images
new_img = Image.fromarray(img_raw)
new_img = np.array(new_img.rotate(direction * angle))
