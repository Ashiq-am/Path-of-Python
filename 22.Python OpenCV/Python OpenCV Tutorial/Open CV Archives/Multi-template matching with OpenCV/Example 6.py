# loop over the final bounding boxes
for (x1, y1, x2, y2) in boxes:
    # draw the bounding box on the image
    cv2.rectangle(img, (x1, y1), (x2, y2),
                  (255, 0, 0), 3)

# Show the template and the final output
cv2.imshow("Template", temp)
cv2.imshow("After NMS", img)
cv2.waitKey(0)
