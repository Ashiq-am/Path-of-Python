# Python code for isinstance()
class Test:
    a = 5


TestInstance = Test()

print(isinstance(TestInstance, Test))
print(isinstance(TestInstance, (list, tuple)))
print(isinstance(TestInstance, (list, tuple, Test)))
