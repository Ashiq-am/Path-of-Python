""



"""

#include <Python.h>

/* Execute func(x, y) in the Python interpreter. The
arguments and return result of the function must
be Python floats */

double call_func(PyObject *func, double x, double y)
{
	PyObject *args;
	PyObject *kwargs;
	PyObject *result = 0;
	double retval;
	
	// Make sure we own the GIL
	PyGILState_STATE state = PyGILState_Ensure();
	
	
	// Verify that func is a proper callable
	if (!PyCallable_Check(func))
	{
		fprintf(stderr, "call_func: expected a callable\n");
		goto fail;
	}



"""