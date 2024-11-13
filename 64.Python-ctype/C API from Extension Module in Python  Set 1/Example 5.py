""



'''
// Module initialization function

PyMODINIT_FUNC
PyInit_sample(void)
{
	PyObject *m;
	PyObject *py_point_api;
	m = PyModule_Create(&samplemodule);
	if (m == NULL)
		return NULL;
		
	// Add the Point C API functions
	py_point_api = PyCapsule_New((void *) &_point_api, "work._point_api", NULL);
	if (py_point_api)
	{
		PyModule_AddObject(m, "_point_api", py_point_api);
	}
	return m;
}



'''