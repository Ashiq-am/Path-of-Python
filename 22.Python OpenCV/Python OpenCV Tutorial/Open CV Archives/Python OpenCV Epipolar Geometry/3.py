def drawlines(img1, img2, lines, pts1, pts2):
    r, c = img1.shape
    img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

    for r, pt1, pt2 in zip(lines, pts1, pts2):
        color = tuple(np.random.randint(0, 255,
                                        3).tolist())

        x0, y0 = map(int, [0, -r[2] / r[1]])
        x1, y1 = map(int,
                     [c, -(r[2] + r[0] * c) / r[1]])

        img1 = cv2.line(img1,
                        (x0, y0), (x1, y1), color, 1)
        img1 = cv2.circle(img1,
                          tuple(pt1), 5, color, -1)
        img2 = cv2.circle(img2,
                          tuple(pt2), 5, color, -1)
    return img1, img2
