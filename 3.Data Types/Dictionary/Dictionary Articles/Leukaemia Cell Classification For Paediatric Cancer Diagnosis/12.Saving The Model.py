# Define a ModelCheckpoint callback
checkpoint = ModelCheckpoint(
	'best_model.h5', # Filepath to save the best model
	monitor='val_loss', # Metric to monitor for improvement
	save_best_only=True, # Save only the best model
	mode='min', # 'min' for val_loss, 'max' for val_accuracy, etc.
	verbose=1 # 1: prints a message for each improvement
)
