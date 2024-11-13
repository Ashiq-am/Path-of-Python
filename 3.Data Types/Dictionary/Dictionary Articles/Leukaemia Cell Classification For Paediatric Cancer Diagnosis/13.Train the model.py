# Train the model with ModelCheckpoint callback
model_trained = model.fit(
	X_train, y_train,
	batch_size=BATCH_SIZE,
	epochs=10,
	validation_data=(X_val, y_val),
	callbacks=[checkpoint] # Add the ModelCheckpoint callback
)
