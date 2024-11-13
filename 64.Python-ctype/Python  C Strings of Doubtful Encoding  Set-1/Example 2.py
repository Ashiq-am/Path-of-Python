""


"""
/* Return the C string back to Python */
static PyObject *py_retstr(PyObject *self, PyObject *args)
{
	if (!PyArg_ParseTuple(args, ""))
	{
		return NULL;
	}
	return PyUnicode_Decode(sdata, slen, "utf-8", "surrogateescape");
}

/* Wrapper for the print_chars() function */
static PyObject *py_print_chars(PyObject *self, PyObject *args)
{
	PyObject *obj, *bytes;
	char *s = 0;
	Py_ssize_t len;
	if (!PyArg_ParseTuple(args, "U", &obj))
	{
		return NULL;
	}
	if ((bytes = PyUnicode_AsEncodedString(obj,
	"utf-8","surrogateescape"))
			== NULL)
	{
		return NULL;
	}
	PyBytes_AsStringAndSize(bytes, &s, &len);
	print_chars(s, len);
	Py_DECREF(bytes);
	Py_RETURN_NONE;
}




"""