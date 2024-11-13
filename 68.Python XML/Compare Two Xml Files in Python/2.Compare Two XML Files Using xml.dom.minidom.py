from xml.dom import minidom
doc1 = minidom.parse('file1.xml')
doc2 = minidom.parse('file2.xml')
diff = doc1.toxml() == doc2.toxml()
if diff:
	print("XML files are same.")
else:
	print("XML files are different.")
