def predict_age(input_path: str):
    """Predict the age of the faces showing in the image"""
    # Read Input Image
    img = cv2.imread(input_path)
    # resize the image
    img = cv2.resize(img, (frame_width, frame_height))
    # Take a copy of the initial image and resize it
    frame = img.copy()
    faces = get_faces(frame)
    for i, (start_x, start_y, end_x, end_y) in enumerate(faces):
            face_img = frame[start_y: end_y, start_x: end_x]
            # image --> Input image to preprocess before passing it through our dnn for classification.
            blob = cv2.dnn.blobFromImage(
                image=face_img, scalefactor=1.0, size=(227, 227),
                mean=MODEL_MEAN_VALUES, swapRB=False
            )
            # Predict Age
            age_net.setInput(blob)
            age_preds = age_net.forward()
            print("="*30, f"Face {i+1} Prediction Probabilities", "="*30)
            for i in range(age_preds[0].shape[0]):
                print(f"{AGE_INTERVALS[i]}: {age_preds[0, i]*100:.2f}%")
            i = age_preds[0].argmax()
            age = AGE_INTERVALS[i]
            age_confidence_score = age_preds[0][i]
            # Draw the box
            label = f"Age:{age} - {age_confidence_score*100:.2f}%"
            print(label)
            # get the position where to put the text
            yPos = start_y - 15
            while yPos < 15:
                yPos += 15
            # write the text into the frame
            cv2.putText(frame, label, (start_x, yPos),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), thickness=2)
            # draw the rectangle around the face
            cv2.rectangle(frame, (start_x, start_y), (end_x, end_y), color=(255, 0, 0), thickness=2)
    # Display processed image
    display_img('Age Estimator', frame)
    # save the image if you want
    # cv2.imwrite("predicted_age.jpg", frame)