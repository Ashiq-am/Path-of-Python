""




"""



static PyObject* py_get_filename(PyObject* self, PyObject* args)
{
	PyObject* bytes;
	char* filename;
	Py_ssize_t len;

	if (!PyArg_ParseTuple(args, "O&", PyUnicode_FSConverter, &bytes)) {
		return NULL;
	}

	PyBytes_AsStringAndSize(bytes, &filename, &len);
	/* Use filename */
	/* Cleanup and return */
	Py_DECREF(bytes)
		Py_RETURN_NONE;
}




"""