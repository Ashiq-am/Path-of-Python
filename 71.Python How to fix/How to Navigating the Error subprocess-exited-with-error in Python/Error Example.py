import subprocess
try:
    result = subprocess.run(['ls', '-la'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
