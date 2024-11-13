def authorize_access(func):
	def wrapper(self, *args, **kwargs):
		if self.is_authorized:
			return func(self, *args, **kwargs)
		else:
			raise PermissionError("Unauthorized access")

	return wrapper

class SecureResource:
	def __init__(self, is_authorized=True):
		self.is_authorized = is_authorized

	@authorize_access
	def sensitive_operation(self):
		print("Access granted. Performing sensitive operation.")
		return "Operation completed."

# Usage
secure_resource = SecureResource(is_authorized=True)
result = secure_resource.sensitive_operation()
