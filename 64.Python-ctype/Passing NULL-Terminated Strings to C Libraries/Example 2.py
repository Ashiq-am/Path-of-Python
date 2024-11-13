""



"""
static PyObject * py_print_chars(PyObject * self, PyObject * args)
{
	char * s;
	if (! PyArg_ParseTuple(args, "y", &s))
	{
		return NULL;
	}
	print_chars(s);
	Py_RETURN_NONE;
}



"""