import json

# Define the custom separator
custom_sep = ';'

# Open the file
with open('jsf.txt', 'r') as file:
    # Read the file content
    file_content = file.read()

    # Split the content using the custom separator
    objects = file_content.split(custom_sep)

    # Process each split part as a separate object
    for obj_str in objects:
        # Parse string into a Python object
        obj = json.loads(obj_str)

        print(obj)
