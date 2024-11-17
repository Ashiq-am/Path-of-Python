import cv2

if __name__ == "__main__":

    findPlate = PlateFinder()
    model = OCR()

    cap = cv2.VideoCapture('test_videos / video.MOV')

    while (cap.isOpened()):
        ret, img = cap.read()

        if ret == True:
            cv2.imshow('original video', img)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

            possible_plates = findPlate.find_possible_plates(img)

            if possible_plates is not None:

                for i, p in enumerate(possible_plates):
                    chars_on_plate = findPlate.char_on_plate[i]
                    recognized_plate, _ = model.label_image_list(
                        chars_on_plate, imageSizeOuput=128)

                    print(recognized_plate)
                    cv2.imshow('plate', p)

                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
