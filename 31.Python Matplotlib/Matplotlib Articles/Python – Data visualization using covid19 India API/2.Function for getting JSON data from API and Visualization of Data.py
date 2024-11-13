#storing the url in the form of string
url="https://api.covid19india.org/state_district_wise.json"

#function to get data from api
def casesData():
	#getting the json data by calling api
	data = ((requests.get(url)).json())
	states = []
