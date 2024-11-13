from transformers import Seq2SeqTrainingArguments

model.to(device)
training_args = Seq2SeqTrainingArguments(
	f"finetuned-nlp-en-hi",
	gradient_checkpointing=True,
	per_device_train_batch_size=32,
	learning_rate=1e-5,
	warmup_steps=2,
	max_steps=2000,
	fp16=True,
	optim='adafactor',
	per_device_eval_batch_size=16,
	metric_for_best_model="eval_bleu",
	predict_with_generate=True,
	push_to_hub=False,
)
