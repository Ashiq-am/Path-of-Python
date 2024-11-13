# import json module
import json

# dictionary of employee data
data = {
	"id": ("1", "2", "3"),
	"name": ("bhanu", "sivanagulu"),
	"department": ("HR", "IT")
}

# convert into json
final = json.dumps(data, indent=2)

# display
print(final)
