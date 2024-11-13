import os

def create_nested_directory(path):
    try:
        os.makedirs(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")

# Example usage:
directory_path = "./parent_directory/child_directory"
create_nested_directory(directory_path)
