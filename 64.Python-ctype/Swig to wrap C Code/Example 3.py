""



'''


// Map int * remainder as an output argument
%include typemaps.i
%apply int * OUTPUT { int * remainder };

// Map the argument pattern (double * a, int n) to arrays
%typemap(in) (double * a, int n)(Py_buffer view)
{
	view.obj = NULL;
	if (PyObject_GetBuffer($input, &view,
						PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1)
	{
		SWIG_fail;
	}
	if (strcmp(view.format, "d") != 0)
	{
		PyErr_SetString(PyExc_TypeError,
						"Expected an array of doubles");
		SWIG_fail;
	}
	$1 = (double *) view.buf;
	$2 = view.len / sizeof(double);
}

% typemap(freearg) (double * a, int n)
{
	if (view$argnum.obj)
	{
		PyBuffer_Release(&view$argnum);
	}
}



'''