""""""



'''
/* Extension function for testing the C-Python callback */

PyObject * py_call_func(PyObject * self, PyObject * args)
{
	PyObject * func;

	double x, y, result;
	if (! PyArg_ParseTuple(args, "Odd", &func, &x, &y))
	{
		return NULL;
	}
	result = call_func(func, x, y);
	return Py_BuildValue("d", result);
}


'''