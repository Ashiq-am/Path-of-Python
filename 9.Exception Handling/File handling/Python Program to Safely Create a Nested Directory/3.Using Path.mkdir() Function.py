from pathlib import Path

def create_nested_directory(path):
    directory = Path(path)
    try:
        directory.mkdir(parents=True)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")

directory_path = "./parent_directory/child_directory"
create_nested_directory(directory_path)
