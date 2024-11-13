import emoji

# Define the string to analyze
text = "Hello ?! Let's grab some ? and ?."

# Analyze the string
tokens = emoji.analyze(text)

for token in tokens:
    print(token)
