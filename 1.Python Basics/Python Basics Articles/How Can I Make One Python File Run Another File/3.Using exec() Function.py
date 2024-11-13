with open('target_file.py', 'r') as file:
    code = file.read()
    exec(code)
