import shutil
import subprocess
if shutil.which('ls') is None:
    print("Error: Command 'ls' not found.")
else:
    try:
        result = subprocess.run(['ls', '-la'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
        print(f"Error output: {e.stderr.decode()}")
