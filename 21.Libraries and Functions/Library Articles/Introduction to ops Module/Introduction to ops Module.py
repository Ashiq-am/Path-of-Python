import ops

# Step 1: Create a folder named 'MyProject'
ops.run('mkdir MyProject')

# Step 2: Navigate into 'MyProject' folder
ops.run('cd MyProject')

# Step 3: Create a text file and write some content into it
with open('example.txt', 'w') as file:
    file.write('Hello, this is a test file.')

# Step 4: Read the content of the file and print it
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
