from xml.dom import minidom
import os

users_list = ["GeeksForGeeks", "Arka", "Computer Science", "Engineering", "Portal"]

# create file
root = minidom.Document()

# creat root element
xml = root.createElement('root')
root.appendChild(xml)

for user in range(len( users_list)):

	# create child element
	productChild = root.createElement('product'+ str(user))

	# insert user data into element
	productChild.setAttribute('list', users_list[user] )
	xml.appendChild(productChild)

xml_str = root.toprettyxml(indent ="\t")

# save file
save_path_file = "gfg.xml"

with open(save_path_file, "w") as f:
	f.write(xml_str)
