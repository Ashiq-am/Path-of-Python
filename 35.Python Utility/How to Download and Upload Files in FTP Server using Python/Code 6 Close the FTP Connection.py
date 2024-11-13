# Display the content of downloaded file
file= open(filename, "r")
print('File Content:', file.read())

# Close the Connection
ftp_server.quit()
