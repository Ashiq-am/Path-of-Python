import subprocess

# Command to execute
command = ["echo", "Hello, World!"]

# Start the subprocess
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Wait for the command to complete and get the output
stdout, stderr = process.communicate()

print("Output:", stdout)
print("Errors:", stderr)
print("Return Code:", process.returncode)
