# horizontally concatenates images
# of same height
im_h = cv2.hconcat([img2, img2])

# show the output image
cv2.imshow('man_image.jpeg', im_h)
