# update first student python subject
# to html
data[0]['subjects'].insert(0, 'html')
data[0]['subjects'].pop(1)

# update third student java subject
# to dbms
data[2]['subjects'].insert(0, 'dbms')
data[2]['subjects'].pop(1)

# update forth student php subject
# to php-mysql
data[3]['subjects'].insert(1, 'php-mysql')
data[3]['subjects'].pop(0)

# display updated list
data
