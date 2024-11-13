article = dataset['validation'][2]['translation']['en']
inputs = tokenizer(article, return_tensors="pt")

translated_tokens = model.generate(
	**inputs, max_length=256
)
tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
