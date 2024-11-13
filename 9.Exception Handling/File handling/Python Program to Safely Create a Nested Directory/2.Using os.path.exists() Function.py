import os

def create_nested_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory '{path}' created successfully.")
    else:
        print(f"Directory '{path}' already exists.")

# Example usage:
directory_path = "./parent_directory/child_directory"
create_nested_directory(directory_path)
