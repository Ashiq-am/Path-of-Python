# Extract Integer or Float from String
def get_number_from_string(string):
	return float(''.join([x for x in string if x.isdigit() or x == '.']))
