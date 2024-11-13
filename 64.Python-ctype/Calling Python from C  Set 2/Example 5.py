""



'''
double call_func(PyObject *func, double x, double y)
{
	...
	// Verify that func is a proper callable
	if (!PyCallable_Check(func))
	{
		fprintf(stderr, "call_func: expected a callable\n");
		goto fail;
	}
	...



'''