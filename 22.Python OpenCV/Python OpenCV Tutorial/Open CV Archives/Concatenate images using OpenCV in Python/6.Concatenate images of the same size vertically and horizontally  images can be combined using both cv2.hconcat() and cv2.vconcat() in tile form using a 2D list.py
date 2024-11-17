# define a function for vertically
# concatenating images of the
# same size and horizontally
def concat_vh(list_2d):
    # return final image
    return cv2.vconcat([cv2.hconcat(list_h)
                        for list_h in list_2d])


# image resizing
img1_s = cv2.resize(img1, dsize=(0, 0),
                    fx=0.5, fy=0.5)

# function calling
img_tile = concat_vh([[img1_s, img1_s, img1_s],
                      [img1_s, img1_s, img1_s],
                      [img1_s, img1_s, img1_s]])
# show the output image
cv2.imshow('concat_vh.jpg', img_tile)
