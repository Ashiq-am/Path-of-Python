file_path = r"C:\Users\R.Daswanta kumar\OneDrive\Pictures\GFG\file\GFG.txt"

with open(file_path, "w") as file:
    new_content = "New content to replace the existing content."
    file.write(new_content)

print("File content modified successfully!")
