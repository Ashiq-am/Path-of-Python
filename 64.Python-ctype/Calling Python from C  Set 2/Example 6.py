""


'''

double call_func(PyObject *func, double x, double y)
	{
		PyObject *args;
		PyObject *kwargs;
		
		/* Build arguments */
		args = Py_BuildValue("(dd)", x, y);
		kwargs = NULL;
		/* Call the function */
		result = PyObject_Call(func, args, kwargs);
		Py_DECREF(args);
		Py_XDECREF(kwargs);
		
		
		/* Check for Python exceptions (if any) */
		if (PyErr_Occurred())
		{
			PyErr_Print();
			goto fail;
		}
		
	fail:
		PyGILState_Release(state);
		abort();
		
	}



'''