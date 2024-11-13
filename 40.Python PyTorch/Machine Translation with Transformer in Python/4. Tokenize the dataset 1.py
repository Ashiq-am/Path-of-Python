tokenized_datasets_validation = dataset['validation'].map(
	preprocess_function,
	batched= True,
	remove_columns=dataset["validation"].column_names,
	batch_size = 2
)

tokenized_datasets_test = dataset['test'].map(
	preprocess_function,
	batched= True,
	remove_columns=dataset["test"].column_names,
	batch_size = 2)
