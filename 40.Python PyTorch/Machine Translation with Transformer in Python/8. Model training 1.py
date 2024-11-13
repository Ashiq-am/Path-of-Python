from transformers import Seq2SeqTrainer

trainer = Seq2SeqTrainer(
	model,
	training_args,
	train_dataset=tokenized_datasets_test,
	eval_dataset=tokenized_datasets_validation,
	data_collator=data_collator,
	tokenizer=tokenizer,
	compute_metrics=compute_metrics,
)

trainer.train()
