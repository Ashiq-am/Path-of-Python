# define a function for concatenating
# images of different sizes in
# vertical and horizontal tiles
def concat_tile_resize(list_2d,
                       interpolation=cv2.INTER_CUBIC):
    # function calling for every
    # list of images
    img_list_v = [hconcat_resize(list_h,
                                 interpolation=cv2.INTER_CUBIC)
                  for list_h in list_2d]

    # return final image
    return vconcat_resize(img_list_v, interpolation=cv2.INTER_CUBIC)


# function calling
im_tile_resize = concat_tile_resize([[img1],
                                     [img1, img2,
                                      img1, img2, img1],
                                     [img1, img2, img1]])
# show the image
cv2.imshow('concat_tile_resize.jpg', im_tile_resize)
