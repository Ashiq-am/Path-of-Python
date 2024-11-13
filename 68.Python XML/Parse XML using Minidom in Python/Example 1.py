import xml.dom.minidom

docs = xml.dom.minidom.parse("test.xml")

print(docs.nodeName)
print(docs.firstChild.tagName)
