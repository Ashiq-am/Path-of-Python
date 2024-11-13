import telnetlib
import getpass


HOST = "localhost"
user = input("USERNAME: ")
password = getpass.getpass()

# MAGIC is the formatted output information
# that we gathered in step 2.
MAGIC = b"\x1b[1;35mpvtejeswar\x1b[0m@\x1b[1;36mmx\x1b[0m:"
tn = telnetlib.Telnet()
tn.open(HOST)

tn.read_until(b"login: ")
tn.write(user.encode("ascii")+b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode("ascii")+b"\n")

# reading untill we reach the
# MAGIC or reading whatever is
# there and timeout after 5 sec.
tn.read_until(MAGIC, 5)

# we write the command to the terminal
tn.write(b"ls -ltr /\n")
print("="*80)
print("output for 'ls -ltr /': ")

# output needs to be decoded to human readable
print(tn.read_until(MAGIC).decode('ascii'))
print("="*80)
tn.write(b"exit\n")

# read everything there is on the comsole
print(tn.read_all().decode('ascii'))
tn.close()
