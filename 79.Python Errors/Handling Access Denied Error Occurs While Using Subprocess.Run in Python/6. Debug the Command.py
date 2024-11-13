import subprocess

# Ensure the script is executable
subprocess.run(['chmod', '+x', '/path/to/your_script.sh'])

# Run the script
result = subprocess.run(['/path/to/your_script.sh'], capture_output=True, text=True)
print(result.stdout)
