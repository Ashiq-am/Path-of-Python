import subprocess

try:
    # Run the command as administrator
    result = subprocess.run(['runas', '/user:Administrator', 'C:\\absolute\\path\\to\\your_script.bat'], capture_output=True, text=True, check=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
except PermissionError:
    print("Permission denied. Please check your permissions.")
