import subprocess

# Arguments to be passed to the called script
arg1 = "Geeks"
arg2 = "for"
arg3 = "Geeks"

# Run the called script with arguments
subprocess.run(['python', 'called_script.py', arg1, arg2, arg3])
