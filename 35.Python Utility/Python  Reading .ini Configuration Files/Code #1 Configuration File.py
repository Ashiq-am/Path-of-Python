''''''


'''

abc.ini 

; Sample configuration file
[installation] 
library = %(prefix)s/lib 
include = %(prefix)s/include 
bin = %(prefix)s/bin
prefix = /usr/local 

# Setting related to debug configuration 
[debug] 
pid-file = /tmp/spam.pid 
show_warnings = False
log_errors = true 
[server] 
nworkers: 32
port: 8080
root = /www/root 
signature: 
'''