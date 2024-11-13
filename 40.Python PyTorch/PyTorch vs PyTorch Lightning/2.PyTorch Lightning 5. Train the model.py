# Initialize the trainer
trainer = pl.Trainer(max_epochs=10, accelerator = "cpu" if torch.cuda.is_available() else "cpu")
