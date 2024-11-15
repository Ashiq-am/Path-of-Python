""

'''

/* Call double avg(double *, int) */
static PyObject *py_avg(PyObject *self, PyObject *args)
{
	PyObject *bufobj;
	Py_buffer view;
	double result;
	/* Get the passed Python object */
	if (!PyArg_ParseTuple(args, "O", &bufobj))
	{
		return NULL;
	}

	/* Attempt to extract buffer information from it */

	if (PyObject_GetBuffer(bufobj, &view,
						PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1)
	{
		return NULL;
	}

	if (view.ndim != 1)
	{
		PyErr_SetString(PyExc_TypeError, "Expected a 1-dimensional array");
		PyBuffer_Release(&view);
		return NULL;
	}

	/* Check the type of items in the array */
	if (strcmp(view.format, "d") != 0)
	{
		PyErr_SetString(PyExc_TypeError, "Expected an array of doubles");
		PyBuffer_Release(&view);
		return NULL;
	}

	/* Pass the raw buffer and size to the C function */
	result = avg(view.buf, view.shape[0]);

	/* Indicate we're done working with the buffer */
	PyBuffer_Release(&view);
	return Py_BuildValue("d", result);
}


'''