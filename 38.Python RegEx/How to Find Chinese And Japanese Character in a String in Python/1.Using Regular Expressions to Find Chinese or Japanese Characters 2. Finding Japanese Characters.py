# import regular expression module
import re

def find_japanese(text):
    # Regex pattern for Hiragana, Katakana, and Kanji (CJK Ideographs)
    japanese_pattern = re.compile(r'[\u3040-\u30FF\u4E00-\u9FFF]')
    return japanese_pattern.findall(text)

# Example usage
text = "これは日本語の文字列です。"
japanese_chars = find_japanese(text)
print("Japanese characters found:", japanese_chars)
