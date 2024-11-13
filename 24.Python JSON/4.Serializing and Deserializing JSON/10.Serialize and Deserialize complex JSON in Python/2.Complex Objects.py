from typing import List
import json


class Student(object):
	def __init__(self, first_name: str, last_name: str):
		self.first_name = first_name
		self.last_name = last_name


class Team(object):
	def __init__(self, students: List[Student]):
		self.students = students


student1 = Student(first_name="Geeky", last_name="Guy")
student2 = Student(first_name="GFG", last_name="Rocks")
team = Team(students=[student1, student2])
json_data = json.dumps(team.__dict__, indent=4)
print(json_data)
