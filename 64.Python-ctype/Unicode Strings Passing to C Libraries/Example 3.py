""



"""

static PyObject *py_print_chars(PyObject *self, PyObject *args)
{
	char *s;
	Py_ssize_t len;
	if (!PyArg_ParseTuple(args, "s#", &s, &len))
	{
		return NULL;
	}
	print_chars(s, len);
	Py_RETURN_NONE;
}


"""