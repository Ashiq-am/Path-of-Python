import subprocess

try:
    # Run the 'echo' command and capture its output
    output = subprocess.check_output(["echo", "Hello, World!"], text=True)
    print("Output:", output)
except subprocess.CalledProcessError as e:
    print("Failed to run command:", e)
