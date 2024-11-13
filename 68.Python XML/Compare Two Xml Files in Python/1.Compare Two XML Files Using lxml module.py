from lxml import etree
tree1 = etree.parse('file1.xml')
tree2 = etree.parse('file2.xml')
diff = etree.tostring(tree1) == etree.tostring(tree2)
if diff:
	print("XML files are same.")
else:
	print("XML files are different.")
