import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print("Return code:", result.returncode)
print("Output:", result.stdout)
print("Error:", result.stderr)
