import xml.dom.minidom as md

def main():

	file = md.parse( "test.xml" )
	names = file.getElementsByTagName( "fname" )

	for name in names:

		print( name.firstChild.nodeValue )

if __name__=="__main__":
	main()
