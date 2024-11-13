import subprocess

process = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
stdout, stderr = process.communicate()

print("Return code:", process.returncode)
print("Output:", stdout)
print("Error:", stderr)
