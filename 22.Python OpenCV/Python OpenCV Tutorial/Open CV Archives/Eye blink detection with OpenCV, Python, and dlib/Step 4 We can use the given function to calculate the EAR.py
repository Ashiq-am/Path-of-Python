def calculate_EAR(eye):
    # calculate the vertical distances
    # euclidean distance is basically
    # the same when you calculate the
    # hypotenuse in a right triangle
    y1 = dist.euclidean(eye[1], eye[5])
    y2 = dist.euclidean(eye[2], eye[4])

    # calculate the horizontal distance
    x1 = dist.euclidean(eye[0], eye[3])

    # calculate the EAR
    EAR = (y1 + y2) / x1

    return EAR
