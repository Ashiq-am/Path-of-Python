# Update/ POST Request
import requests

url = "https://fruits-api.netlify.app/graphql"

body = """
mutation {
updateFruit(
	id: 1
	scientific_name: "mangiferaa"
	tree_name: "mangifera indicaa"
	fruit_name: "Mangooo"
	family: "Anacardiaceae"
	origin: "Indiana"
	description: "Mango is green"
	bloom: "Summer"
	maturation_fruit: "Mango"
	life_cycle: "101"
	climatic_zone: "humid"
) {
	id
	scientific_name
	tree_name
	fruit_name
	description
}
}
"""
response = requests.post(url=url, json={"query": body})
print("response status code: ", response.status_code)
if response.status_code == 200:
	print("response : ", response.content)
