class A:
	@staticmethod
	def m() -> int:
		return 1

class B(A):
	@staticmethod
	def m() -> int:
		return super().m()

B().m()
