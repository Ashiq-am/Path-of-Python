def drawRectangle(image, a, b, c, d, low_threshold, high_threshold, min_pix, max_pix):
    sub_image = image[b:b + d, a:a + c]
    edges = cv2.Canny(sub_image, low_threshold, high_threshold)
    pix = cv2.countNonZero(edges)
    if pix in range(min_pix, max_pix):
        cv2.rectangle(image, (a, b), (a + c, b + d), (0, 255, 0), 3)
        Spots.location += 1
    else:
        cv2.rectangle(image, (a, b), (a + c, b + d), (0, 0, 255), 3)
