class EarlyStopping:
    def __init__(self, patience=3):
        self.patience = patience
        self.counter = 0
        self.best_loss = None

    def on_epoch_end(self, epoch, logs=None):
        current_loss = logs['loss']
        if self.best_loss is None or current_loss < self.best_loss:
            self.best_loss = current_loss
            self.counter = 0
        else:
            self.counter += 1
            if self.counter >= self.patience:
                logging.info("Early stopping triggered.")
                return True
        return False
