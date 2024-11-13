# Opening the existing HTML file
Func = open("GFG-2.html","w")

# Adding input data to the HTML file
Func.write("<html>\n<head>\n<title> \nOutput Data in an HTML file\n \
		</title>\n</head> <body> <h1>Welcome to \
		<font color = #00b300>GeeksforGeeks</font></h1>\n \
		<h2>A CS Portal for Everyone</h2>\n</body></html>")

# Saving the data into the HTML file
Func.close()
