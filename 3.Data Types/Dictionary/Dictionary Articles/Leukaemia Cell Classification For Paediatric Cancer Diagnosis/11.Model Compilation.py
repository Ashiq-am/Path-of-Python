model = Sequential()
model.add(Conv2D(filters=2, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=input_shape))
model.add(Conv2D(filters=4, kernel_size=(3, 3), padding='valid', activation='relu'))
model.add(Conv2D(filters=8, kernel_size=(5, 5), padding='valid', activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Dropout(0.5))

model.add(Conv2D(filters=16, kernel_size=(5, 5), padding='valid', activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(Flatten())

model.add(Dense(8, kernel_regularizer=l2(1e-5), activation="relu"))
model.add(BatchNormalization())

model.add(Dense(1, activation="sigmoid"))
model.summary()
