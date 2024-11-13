# code
import paramiko

try:
    # Setup SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.1.1', username='admin', password='adminpassword')
    print("SSH connection established.")

    # Setup SFTP session
    sftp = ssh.open_sftp()
    print("SFTP session started.")

    sftp.get('/home/admin/report.txt', '/home/admin/copied_report.txt')
    print("File transfer successful.")

finally:
    if sftp: sftp.close()
    if ssh: ssh.close()
    print("Connections closed.")
