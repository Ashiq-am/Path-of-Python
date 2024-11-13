# importing the module
import imdb

# creating instance of IMDb
ia = imdb.IMDb()

# id
code = "0051941"

# getting information
company = ia.get_company(code)

# printing company
print(company)

print("--------------------------------")

# converting company object into XML file
xml_file = company.asXML()

# printing some part of the XML file
print(xml_file[:250])
