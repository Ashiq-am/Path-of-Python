# import library
from typing import List, Dict

# define function
def get_list_of_dicts(name: str, category: str) -> Dict[str, str]:
	return [{'name': name, 'category': category}]

Fruit = ["Mango", "tomato", "potato", "papaya"]
Fruit_type = ["fruit", "vegetable", "vegetable", "fruit"]

res = [get_list_of_dicts(Fruit[i], Fruit_type[i]) for i in range(3)]

print(res)
