# Loop through each component
for i in range(1, totalLabels):
    area = values[i, cv2.CC_STAT_AREA]

    if (area > 140) and (area < 400):
        # Labels stores all the IDs of the components on the each pixel
        # It has the same dimension as the threshold
        # So we'll check the component
        # then convert it to 255 value to mark it white
        componentMask = (label_ids == i).astype("uint8") * 255

        # Creating the Final output mask
        output = cv2.bitwise_or(output, componentMask)
