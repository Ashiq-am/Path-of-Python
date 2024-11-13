# Define the event handlers
@trainer.on(Events.ITERATION_COMPLETED(every=100))
def log_training_loss(trainer):
    print(f"Epoch[{trainer.state.epoch}] Iteration[{trainer.state.iteration}] Loss: {trainer.state.output:.2f}")

@trainer.on(Events.EPOCH_COMPLETED)
def log_training_results(trainer):
    evaluator.run(test_loader)
    metrics = evaluator.state.metrics
    print(f"Training Results - Epoch: {trainer.state.epoch}  Accuracy: {metrics['accuracy']:.2f}")

# Run the trainer
trainer.run(train_loader, max_epochs=10)
