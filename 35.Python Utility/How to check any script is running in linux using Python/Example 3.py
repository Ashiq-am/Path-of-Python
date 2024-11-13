import subprocess


pytonProcess = subprocess.check_output("ps -ef | grep .php",shell=True).decode()
PHPProcess = pytonProcess.split('\n')

for process in PHPProcess:
	print(process)
