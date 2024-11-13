""



'''

PyMODINIT_FUNC
PyInit_ptexample(void)
{
	PyObject *m;
	
	m = PyModule_Create(&ptexamplemodule);
	
	if (m == NULL)
		return NULL;
	
	/* Import sample, loading its API functions */
	if (!import_sample())
	{
		return NULL;
	}
	
	return m;
}



'''