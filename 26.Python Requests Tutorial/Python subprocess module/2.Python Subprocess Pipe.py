import subprocess

lsProcess = subprocess.Popen(["ls"], stdout=subprocess.PIPE, text=True)
grepProcess = subprocess.Popen(
	["grep", "sample"], stdin=ls_process.stdout,
	stdout=subprocess.PIPE, text=True)
output, error = grepProcess.communicate()

print(output)
print(error)
