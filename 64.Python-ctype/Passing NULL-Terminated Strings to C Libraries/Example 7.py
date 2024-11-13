""



"""


{

	PyObject *bytes;
	char *s;

	if (!PyUnicode_Check(obj))
	{
		PyErr_SetString(PyExc_TypeError, "Expected string");
		return NULL;
	}

	bytes = PyUnicode_AsUTF8String(obj);
	s = PyBytes_AsString(bytes);
	print_chars(s);
	Py_DECREF(bytes);
}



"""