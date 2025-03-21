# define a function for vertically
# concatenating images of different
# widths
def vconcat_resize(img_list, interpolation = cv2.INTER_CUBIC):
    # take minimum width
    w_min = min(img.shape[1]
                for img in img_list)

    # resizing images
    im_list_resize = [cv2.resize(img,
                                 (w_min, int(img.shape[0] * w_min / img.shape[1])),
                                 interpolation=interpolation)
                      for img in img_list]
    # return final image
    return cv2.vconcat(im_list_resize)


# function calling
img_v_resize = vconcat_resize([img1, img2, img1])

# show the output image
cv2.imwrite('vconcat_resize.jpg', img_v_resize)
