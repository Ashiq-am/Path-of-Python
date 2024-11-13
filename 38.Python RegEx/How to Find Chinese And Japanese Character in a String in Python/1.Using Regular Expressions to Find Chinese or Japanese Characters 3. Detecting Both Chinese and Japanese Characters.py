import re

def find_cjk(text):
    # Regex pattern for CJK characters (Chinese, Japanese)
    cjk_pattern = re.compile(r'[\u3040-\u30FF\u3400-\u4DBF\u4E00-\u9FFF]')
    return cjk_pattern.findall(text)

# Example usage
text = "This string contains 漢字 and カタカナ."
cjk_chars = find_cjk(text)
print("CJK characters found:", cjk_chars)
