def message_and_history(input, history):
	history = history or []
	print(history)
	s = list(sum(history, ()))
	print(s)
	s.append(input)
	print('#########################################')
	print(s)
	inp = ' '.join(s)
	print(inp)
	output = api_calling(inp)
	history.append((input, output))
	print('------------------')
	print(history)
	print(history)
	print("*********************")
	return history, history
