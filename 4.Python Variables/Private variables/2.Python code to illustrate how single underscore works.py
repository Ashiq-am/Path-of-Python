# Python code to illustrate
# how single underscore works
def _get_errors(self):
	if self._errors is None:
		self.full_clean()
	return self._errors

errors = property(_get_errors)
