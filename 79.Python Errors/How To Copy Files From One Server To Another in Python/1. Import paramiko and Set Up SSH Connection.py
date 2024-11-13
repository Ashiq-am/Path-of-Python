# code
import paramiko

# Establishing an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the source server
source_ip = "192.168.1.1"
source_username = "your_username"
source_password = "your_password"
ssh.connect(source_ip, username=source_username, password=source_password)
