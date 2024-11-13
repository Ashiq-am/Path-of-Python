def preprocess_function(examples):
    inputs = [ex["en"] for ex in examples["translation"]]
    targets = [ex["hi"] for ex in examples["translation"]]


    model_inputs = tokenizer(inputs, max_length=max_length, truncation=True)
    labels = tokenizer(targets,max_length=max_length, truncation=True)
    model_inputs["labels"] = labels["input_ids"]

    return model_inputs
