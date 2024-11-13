# creating nd viewing the html files in python

import webbrowser
import os

# to open/create a new html file in the write mode
f = open('GFG.html', 'w')

# the html code which will go in the file GFG.html
html_template = """ 
<html> 
<head></head> 
<body> 
<p>Geeks For Geeks</p> 

</body> 
</html> 
"""
# writing the code into the file
f.write(html_template)

# close the file
f.close()

# 1st method how to open html files in chrome using
filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
webbrowser.open_new_tab(filename)
