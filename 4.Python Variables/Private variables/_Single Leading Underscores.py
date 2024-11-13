"""So basically one underline in the beginning of a method, function or data member means you shouldn’t access this
method because it’s not part of the API. Let’s look at this snippet of code:"""



# Python code to illustrate
# how single underscore works
def _get_errors(self):
	if self._errors is None:
		self.full_clean()
	return self._errors

errors = property(_get_errors)






"""The snippet is taken from Django source code (django/forms/forms.py). This suggests that errors is a property, 
and it’s also a part of the API, but the method, _get_errors, is “private”, so one shouldn’t access it."""