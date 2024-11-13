import subprocess

output = subprocess.check_output(['ls', '-l'], text=True)
print("Output:", output)
