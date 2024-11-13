from ftplib import FTP

ftp = FTP('ftp.us.debian.org')

ftp.login()

# changing directory
ftp.cwd('debian')

ftp.nlst()

ftp.quit()
