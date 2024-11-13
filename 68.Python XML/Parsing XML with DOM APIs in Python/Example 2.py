from xml.dom import minidom

doc = minidom.parse("sample.xml")

# doc.getElementsByTagName returns the NodeList
name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

staffs = doc.getElementsByTagName("staff")
for staff in staffs:
		staff_id = staff.getAttribute("id")
		name = staff.getElementsByTagName("name")[0]
		salary = staff.getElementsByTagName("salary")[0]
		print("id:% s, name:% s, salary:% s" %
			(staff_id, name.firstChild.data, salary.firstChild.data))
