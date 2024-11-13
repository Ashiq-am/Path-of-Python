def contains_japanese(text):
    for char in text:
        if '\u3040' <= char <= '\u30FF' or '\u4E00' <= char <= '\u9FFF':
            return True
    return False

# Example usage
text = "これはテストです。"
if contains_japanese(text):
    print("Japanese characters detected.")
else:
    print("No Japanese characters found.")
