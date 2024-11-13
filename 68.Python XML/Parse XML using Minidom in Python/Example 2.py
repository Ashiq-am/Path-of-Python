import xml.dom.minidom


docs = xml.dom.minidom.parse("test.xml")

print(docs.nodeName)
print(docs.firstChild.tagName)

skills = docs.getElementsByTagName("skills")

print("%d skills" % skills.length)
for i in skills:
	print(i.getAttribute("name"))
