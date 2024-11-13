# import json module
from google.colab import files
import json

# dictionary of employee data
data = {
	"id": ("1", "2", "3"),
	"name": ("bhanu", "sivanagulu"),
	"department": ("HR", "IT")
}

# convert into json
# file name is mydata
with open("mydata.json", "w") as final:
	json.dump(data, final)

# download the json file
files.download('mydata.json')
