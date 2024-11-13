""



"""

/* Object with the filename */
PyObject* obj;
PyObject* bytes;

char* filename;
Py_ssize_t len;

bytes = PyUnicode_EncodeFSDefault(obj);
PyBytes_AsStringAndSize(bytes, &filename, &len);

/* Use filename */
...
	/* Cleanup */
	Py_DECREF(bytes);



"""