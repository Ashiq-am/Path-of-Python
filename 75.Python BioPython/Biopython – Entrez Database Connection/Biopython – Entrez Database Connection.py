# Import libraries
from Bio import Entrez

# Setting email
Entrez.email = 'jeetesh1@yopmail.com'

# Setting Entrez tool parameter
Entrez.tool = 'Demoscript'

# Gathering information
info = Entrez.einfo()

# Reading Info as XML
#data = info.read()

# Parsing info as python object
record = Entrez.read(info)

# Getting record key
record.keys()

# Parsing records
record[u'DbList']
