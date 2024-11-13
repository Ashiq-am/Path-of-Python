import string


def validate_filename(filename):
    forbidden_characters = string.punctuation

    for char in filename:
        if char in forbidden_characters:
            return False, "Invalid filename"

    return True, "Valid filename"


filename1 = "screenshot 26092024 2564.png"
filename2 = "Screenshot 34&911%262.JPEG."

print(f"{filename1}: {validate_filename(filename1)}")
print(f"{filename2}: {validate_filename(filename2)}")
