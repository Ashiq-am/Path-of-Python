#Compile the model
model.compile(optimizer='adam',
			loss='categorical_crossentropy',
			metrics=['accuracy'])

#Train the model
model.fit(X_train, y_train, epochs=100, batch_size=4, verbose=1)

#Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss:.4f}')
print(f'Test Accuracy: {accuracy:.4f}')

#Save the model
model.save('iris_model.h5')
