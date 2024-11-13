# Define a string
string_match="Geeks For Geeks"

# Creating first test case
def test_remove_G():
	assert string_match.replace('G','')=="eeks For eeks"

# Creating second test case
def test_remove_e():
	assert string_match.replace('e','')=="Gaks For Gaks"

# Creating third test case
def test_remove_o():
	assert string_match.replace('o','')=="Geeks For Geeks"
