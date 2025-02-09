class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)

    def display(self):
        print(f"Student: {self.name}")
        print(f"Total Marks: {self.total()}")
        print(f"Average Marks: {self.average()}")

# Example usage:
sr = StudentResult("Bob", [76, 84, 90])
sr.display()
