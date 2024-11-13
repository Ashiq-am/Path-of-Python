import xml.dom.minidom as md

def main():

	# parsing the xml file and
	# storing the contents in
	# "file" object Put in the
	# path of your XML file in
	# the parameter for parse() method.
	file = md.parse( "test.xml" )

	# nodeName returns the type of
	# the file(in our case it returns
	# document)
	print( file.nodeName )

	# firstChild.tagName returns the
	# name of the first tag.Here it
	# is "note"
	print( file.firstChild.tagName )

	firstname = file.getElementsByTagName( "fname" )

	# printing the first name
	print( "Name: " + firstname[ 0 ].firstChild.nodeValue )

	lastname = file.getElementsByTagName( "lname" )

	# printing the last name
	print( "Surname: " + lastname[ 0 ].firstChild.nodeValue )

	favgame = file.getElementsByTagName( "favgame" )

	# printing the favourite game
	print( "Favourite Game: " + favgame[ 0 ].firstChild.nodeValue )

	# Printing tag values having
	# attributes(Here tag "player"
	# has "name" attribute)
	players = file.getElementsByTagName( "player" )

	for player in players:
		print( player.getAttribute( "name" ) )

if __name__=="__main__":
	main()
