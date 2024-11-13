import subprocess
import os
file_path = '/path/to/your/file'
if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' does not exist.")
else:
    try:
        result = subprocess.run(['cat', file_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        print(f"Error output: {e.stderr.decode()}")
