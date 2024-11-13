""


"""
/* Call read() */
if ((data = PyObject_Call(read_meth, read_args, NULL)) == NULL) {
	goto final;
}

/* Check for EOF */
if (PySequence_Length(data) == 0) {
	Py_DECREF(data);
	break;
}

if (!PyBytes_Check(data)) {
	Py_DECREF(data);
	PyErr_SetString(PyExc_IOError, "File must be in binary mode");
	goto final;
}

/* Extract underlying buffer data */
PyBytes_AsStringAndSize(data, &buf, &len);



"""