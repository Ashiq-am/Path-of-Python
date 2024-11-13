# Define evaluate_model function
def evaluate_model(model, iterator, criterion):
    model.eval()
    total_correct = 0
    total_examples = 0
    with torch.no_grad():
        for batch in iterator:
            text, text_lengths = batch.text
            predictions = model(text, text_lengths).squeeze(1)
            rounded_preds = torch.round(torch.sigmoid(predictions))
            total_correct += (rounded_preds == batch.label).sum().item()
            total_examples += batch.label.size(0)
    accuracy = total_correct / total_examples
    return accuracy

accuracy = evaluate_model(model, valid_iterator, criterion)
print(f'Validation Accuracy: {accuracy * 100:.2f}%')
