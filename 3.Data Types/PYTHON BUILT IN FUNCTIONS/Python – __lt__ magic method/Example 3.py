class GFG:
	def __init__(self, Marks):
		self.Marks = Marks
	def __lt__(self, marks):
		return self.Marks < marks.Marks

student1_marks = GFG(90)
student2_marks = GFG(88)

print(student1_marks < student2_marks)
print(student2_marks < student1_marks)
