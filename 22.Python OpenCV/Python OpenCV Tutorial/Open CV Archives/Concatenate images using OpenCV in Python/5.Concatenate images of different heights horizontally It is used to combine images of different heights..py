# define a function for horizontally
# concatenating images of different
# heights
def hconcat_resize(img_list,
                   interpolation
                   =cv2.INTER_CUBIC):
    # take minimum hights
    h_min = min(img.shape[0]
                for img in img_list)

    # image resizing
    im_list_resize = [cv2.resize(img,
                                 (int(img.shape[1] * h_min / img.shape[0]),
                                  h_min), interpolation
                                 =interpolation)
                      for img in img_list]

    # return final image
    return cv2.hconcat(im_list_resize)


# function calling
img_h_resize = hconcat_resize([img1, img2, img1])

# show the Output image
cv2.imshow('hconcat_resize.jpg', img_h_resize)
