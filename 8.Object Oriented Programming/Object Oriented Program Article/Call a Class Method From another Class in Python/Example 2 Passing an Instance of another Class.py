class ClassX:
	def method_in_class_x(self):
		print("Method in ClassX")

class ClassY:
	def call_method_from_class_x(self):
		instance_x = ClassX()
		instance_x.method_in_class_x()
		print("Method in ClassY")

# Create an instance of ClassY
obj_y = ClassY()

# Call the method in ClassY, which in turn creates an instance of ClassX and calls its method
obj_y.call_method_from_class_x()
