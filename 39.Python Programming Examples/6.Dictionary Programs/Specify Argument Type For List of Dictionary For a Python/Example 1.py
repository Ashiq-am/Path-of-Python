# typing is a standard library
from typing import List, Dict


def GetData(name: str, age: int) -> List[Dict[str, int]]:
	return [{'name': name, 'age': age}]

print(GetData('Sandeep Jain', 35))
