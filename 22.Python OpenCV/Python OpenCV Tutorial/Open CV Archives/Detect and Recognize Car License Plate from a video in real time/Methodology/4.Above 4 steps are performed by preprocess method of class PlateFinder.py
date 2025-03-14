import cv2


def preprocess(self, input_img):
    imgBlurred = cv2.GaussianBlur(input_img, (7, 7), 0)

    # convert to gray
    gray = cv2.cvtColor(imgBlurred,
                        cv2.COLOR_BGR2GRAY)

    # sobelX to get the vertical edges
    sobelx = cv2.Sobel(gray, cv2.CV_8U,1, 0, ksize=3)

    # otsu's thresholding
    ret2, threshold_img = cv2.threshold(sobelx, 0, 255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    element = self.element_structure
    morph_n_thresholded_img = threshold_img.copy()
    cv2.morphologyEx(src=threshold_img,op=cv2.MORPH_CLOSE,kernel=element,dst=morph_n_thresholded_img)

    return morph_n_thresholded_img
