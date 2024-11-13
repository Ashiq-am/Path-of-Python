""



"""

static PyObject *py_print_chars(PyObject *self, PyObject *args)
{
	char *s;
	Py_ssize_t len;
	
	// accepts bytes, bytearray, or other byte-like object
	
	if (!PyArg_ParseTuple(args, "y#", &s, &len))
	{
		return NULL;
	}
	print_chars(s, len);
	Py_RETURN_NONE;
}


"""