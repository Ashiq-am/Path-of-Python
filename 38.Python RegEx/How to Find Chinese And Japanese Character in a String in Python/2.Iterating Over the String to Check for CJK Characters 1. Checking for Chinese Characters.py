def contains_chinese(text):
    for char in text:
        if '\u4E00' <= char <= '\u9FFF' or '\u3400' <= char <= '\u4DBF':
            return True
    return False

# Example usage
text = "This sentence contains 中文."
if contains_chinese(text):
    print("Chinese characters detected.")
else:
    print("No Chinese characters found.")
