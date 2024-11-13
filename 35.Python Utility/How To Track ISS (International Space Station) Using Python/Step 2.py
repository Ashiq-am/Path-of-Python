file = open("iss.txt", "w")
file.write(
"There are currently " + str(result["number"]) +
" astronauts on the ISS: \n\n")

people = result["people"]
for p in people:
	file.write(p['name'] + " - on board" + "\n")
