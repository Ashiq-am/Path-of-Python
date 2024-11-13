def open_file():
    return "File opened"

def save_file():
    return "File saved"

def close_file():
    return "File closed"

commands = {
    'open': open_file,
    'save': save_file,
    'close': close_file
}

# Executing commands
print(commands['open']())
print(commands['save']())
print(commands['close']())
