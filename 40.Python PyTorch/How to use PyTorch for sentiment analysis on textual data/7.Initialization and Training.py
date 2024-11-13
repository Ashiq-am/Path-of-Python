# Create iterators
train_iterator, valid_iterator = BucketIterator.splits(
    (train_data, test_data), batch_size=64, sort_key=lambda x: len(x.text), shuffle=True
)
# Define hyperparameters
vocab_size = len(TEXT.vocab)
embedding_dim = 100
hidden_dim = 256
output_dim = 1  # Binary classification
# Create model, optimizer, and criterion objects
model = SentimentModel(vocab_size, embedding_dim, hidden_dim, output_dim)
optimizer = optim.Adam(model.parameters())
criterion = nn.BCEWithLogitsLoss()

# Training the model
def train_model(model, iterator, optimizer, criterion, epochs=3):
    model.train()
    for epoch in range(epochs):
        epoch_loss = 0
        for batch in iterator:
            optimizer.zero_grad()
            text, text_lengths = batch.text
            predictions = model(text, text_lengths).squeeze(1)
            loss = criterion(predictions, batch.label)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
        print(f'Epoch {epoch+1}/{epochs}, Loss: {epoch_loss / len(iterator):.4f}')
train_model(model, train_iterator, optimizer, criterion)
