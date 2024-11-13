import subprocess
ans = subprocess.call(["python", "--version"])
if ans == 0:
	print("Command executed.")
else:
	print("Command failed.", return_code)
