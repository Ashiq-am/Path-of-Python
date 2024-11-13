import subprocess

# Absolute path to the script
script_path = '/absolute/path/to/your_script.sh'

# Run the script
result = subprocess.run([script_path], capture_output=True, text=True)
print(result.stdout)
