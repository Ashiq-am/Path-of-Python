from pathlib import Path

file_path = Path('example.txt')

file_content = file_path.read_text()

print(file_content)
