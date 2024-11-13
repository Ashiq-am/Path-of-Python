from xml.dom import minidom

doc = minidom.parse("sample.xml")

# user-defined function
def getNodeText(node):

	nodelist = node.childNodes
	result = []
	for node in nodelist:
		if node.nodeType == node.TEXT_NODE:
			result.append(node.data)
	return ''.join(result)

name = doc.getElementsByTagName("name")[0]
print("Company Name : % s \n" % getNodeText(name))


staffs = doc.getElementsByTagName("staff")
for staff in staffs:
		staff_id = staff.getAttribute("id")
		name = staff.getElementsByTagName("name")[0]
		salary = staff.getElementsByTagName("salary")[0]
		print("id:% s, name:% s, salary:% s" %
			(staff_id, getNodeText(name), getNodeText(salary)))
