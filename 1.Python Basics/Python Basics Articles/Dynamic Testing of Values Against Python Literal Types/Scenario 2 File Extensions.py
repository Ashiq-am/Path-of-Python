# code
FileExtension = Literal['.txt', '.pdf', '.docx']

def is_file_extension(value) -> bool:
    return is_literal_value(value, FileExtension)

print(is_file_extension('.txt'))
print(is_file_extension('.exe'))
