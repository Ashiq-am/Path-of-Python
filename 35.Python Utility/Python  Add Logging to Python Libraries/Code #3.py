""""""



'''

import logging 

logging.basicConfig(level = logging.ERROR) 

import abc 
print (abc.func()) 

Change the logging level for 'abc' only 
logging.getLogger('abc').level = logging.DEBUG 
print (abc.func()) 


'''