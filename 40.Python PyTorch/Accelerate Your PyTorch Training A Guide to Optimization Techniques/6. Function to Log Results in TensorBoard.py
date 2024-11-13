# Function to log results in TensorBoard
def log_results(writer, epoch, loss, accuracy):
    writer.add_scalar('Loss/train', loss, epoch)
    writer.add_scalar('Accuracy/val', accuracy, epoch)
