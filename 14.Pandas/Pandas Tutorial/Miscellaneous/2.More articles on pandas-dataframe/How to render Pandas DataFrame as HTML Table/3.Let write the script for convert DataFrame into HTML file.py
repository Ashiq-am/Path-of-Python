''''''

"""Note: The HTML file will be created with HTML data in the current 
working directory."""



html = df.to_html()

# write html to file
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()
