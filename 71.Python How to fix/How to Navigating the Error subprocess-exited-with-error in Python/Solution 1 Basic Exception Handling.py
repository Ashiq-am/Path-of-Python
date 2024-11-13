import subprocess
try:
    result = subprocess.run(['ls', '-la'], check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Command '{e.cmd}' returned non-zero exit status {e.returncode}.")
