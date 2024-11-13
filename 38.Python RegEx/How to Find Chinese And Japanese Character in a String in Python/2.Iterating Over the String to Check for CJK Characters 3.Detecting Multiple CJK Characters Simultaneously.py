def detect_cjk_languages(text):
    has_chinese = any('\u4E00' <= char <= '\u9FFF' or
                      '\u3400' <= char <= '\u4DBF' for char in text)
    has_japanese = any('\u3040' <= char <= '\u30FF' or
                       '\u4E00' <= char <= '\u9FFF' for char in text)

    if has_chinese:
        print("Chinese characters detected.")
    if has_japanese:
        print("Japanese characters detected.")
    if not has_chinese and not has_japanese:
        print("No CJK characters detected.")


# Example usage
text = "これはテストです and this contains 漢字."
detect_cjk_languages(text)
