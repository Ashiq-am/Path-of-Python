import paramiko

# Create object of SSHClient and
# connecting to SSH
ssh = paramiko.SSHClient()
ssh.connect('1.1.1.2', port=22, username='UserName',
			password='PassWord', timeout=3)

# Adding new host key to the local
# HostKeys object(in case of missing)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Execute command on SSH terminal
# using exec_command
stdin, stdout, stderr = ssh.exec_command('show ip interface brief')
