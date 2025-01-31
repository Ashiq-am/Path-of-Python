def train_model(label):
    # Create lists to store the face samples and their corresponding labels
    faces = []
    labels = []

    # Load the images from the 'Faces' folder
    for file_name in os.listdir('Faces'):
        if file_name.endswith('.jpg'):
            # Extract the label (person's name) from the file name
            name = file_name.split('_')[0]

            # Read the image and convert it to grayscale
            image = cv2.imread(os.path.join('Faces', file_name))
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the grayscale image
            detected_faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Check if a face is detected
            if len(detected_faces) > 0:
                # Crop the detected face region
                face_crop = gray[detected_faces[0][1]:detected_faces[0][1] + detected_faces[0][3],
                            detected_faces[0][0]:detected_faces[0][0] + detected_faces[0][2]]

                # Append the face sample and label to the lists
                faces.append(face_crop)
                labels.append(label[name])

    # Train the face recognition model using the faces and labels
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(labels))

    # Save the trained model to a file
    recognizer.save('trained_model.xml')
    return recognizer


# Train the model
Recognizer = train_model(label)
Recognizer
