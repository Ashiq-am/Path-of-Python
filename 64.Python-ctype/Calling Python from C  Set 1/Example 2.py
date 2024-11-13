""


'''
	// Step3
	args = Py_BuildValue("(dd)", x, y);
	kwargs = NULL;
	
	// Step 4
	result = PyObject_Call(func, args, kwargs);
	Py_DECREF(args);
	Py_XDECREF(kwargs);
	
	// Step 5
	if (PyErr_Occurred())
	{
		PyErr_Print();
		goto fail;
	}
	
	// Verify the result is a float object
	if (!PyFloat_Check(result))
	{
		fprintf(stderr, "call_func: callable didn't return a float\n");
		goto fail;
	}
	
	// Step 6
	retval = PyFloat_AsDouble(result);
	Py_DECREF(result);
	
	// Step 7
	PyGILState_Release(state);
	return retval;
	fail:
		Py_XDECREF(result);
		PyGILState_Release(state);
		abort();
}



'''