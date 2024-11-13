class Geeks:
	website = "GeeksforGeeks"

# original value
print("Original Value: " + Geeks.website)

# editing using setattr()
setattr(Geeks, 'website', 'GFG')
print("Edited Value: " +Geeks.website)
