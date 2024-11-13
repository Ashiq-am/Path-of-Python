""



"""

#include <Python.h>
/* Definition of call_func() same as above */

/* Load a symbol from a module */
PyObject *import_name(const char *modname, const char *symbol)
{
	PyObject *u_name, *module;
	u_name = PyUnicode_FromString(modname);
	module = PyImport_Import(u_name);
	Py_DECREF(u_name);
	
	return PyObject_GetAttrString(module, symbol);
}


"""