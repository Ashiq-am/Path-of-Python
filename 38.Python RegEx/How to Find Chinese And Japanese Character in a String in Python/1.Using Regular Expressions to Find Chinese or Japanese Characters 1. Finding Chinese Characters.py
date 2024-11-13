import re

def find_chinese(text):
    # Regex pattern for Chinese characters (CJK Unified Ideographs)
    chinese_pattern = re.compile(r'[\u4E00-\u9FFF]')
    return chinese_pattern.findall(text)

# Example usage
text = "This is an example string 包含中文字符."
chinese_chars = find_chinese(text)
print("Chinese characters found:", chinese_chars)
