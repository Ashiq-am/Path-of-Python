string_match="Geeks For Geeks"

def test_remove_G():
	assert string_match.replace('G','')=="eks For eeks"

def test_remove_e():
	assert string_match.replace('e','')=="Gaks For Gaks"

def test_remove_o():
	assert string_match.replace('o','')=="Geeks For Geeks"
