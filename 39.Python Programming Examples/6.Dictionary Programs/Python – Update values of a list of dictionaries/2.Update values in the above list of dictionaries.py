# update first student python subject
# to html
data[0]['subjects'].append('html')
data[0]['subjects'].pop(1)

# update third student java subject
# to dbms
data[2]['subjects'].append('dbms')
data[2]['subjects'].pop(1)

# update forth student php subject
# to php-mysql
data[3]['subjects'].append('php-mysql')
data[3]['subjects'].pop(0)

# display updated list
data
