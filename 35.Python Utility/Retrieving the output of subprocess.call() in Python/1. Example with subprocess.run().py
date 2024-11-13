import subprocess

# Run the 'echo' command and capture its output
result = subprocess.run(["echo", "Hello, World!"], capture_output=True, text=True)

# Accessing the output
print("Output:", result.stdout)
print("Return Code:", result.returncode)
