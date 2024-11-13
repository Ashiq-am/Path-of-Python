import subprocess

try:
    # Run the script as root
    result = subprocess.run(['sudo', '/absolute/path/to/your_script.sh'], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
except PermissionError:
    print("Permission denied. Please check your permissions.")
