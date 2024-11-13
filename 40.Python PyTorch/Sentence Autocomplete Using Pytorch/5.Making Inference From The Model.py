# Input a sentence
input_sentence = "he is your "

# Preprocess the input sentence
input_indexes = [dataset.word_to_index[word] for\
				word in input_sentence.split()]
input_tensor = torch.tensor(input_indexes, \
							dtype=torch.long).unsqueeze(0)

# Generate the next word
model.eval()
hidden = model.init_state(len(input_indexes))
outputs, _ = model(input_tensor, hidden)
predicted_index = torch.argmax(outputs[0, -1, :]).item()
predicted_word = dataset.index_to_word[predicted_index]

# Print the predicted word
print("Input Sentence:", input_sentence)
print("Predicted Next Word:", predicted_word)
