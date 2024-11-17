# Loop over the contours to find the document
for c in contours:
    # Approximate the contour
    epsilon = 0.02 * cv2.arcLength(c, True)
    corners = cv2.approxPolyDP(c, epsilon, True)
    # If our approximated contour has four points, we assume it's the document
    if len(corners) == 4:
        break

# Draw the contours and corners on the image
con = np.zeros_like(image)
cv2.drawContours(con, [c], -1, (0, 255, 255), 3)
cv2.drawContours(con, [corners], -1, (0, 255, 0), 10)

# Sort corners and label them
corners = sorted(np.concatenate(corners).tolist())
for index, corner in enumerate(corners):
    character = chr(65 + index)
    cv2.putText(con, character, tuple(corner), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
