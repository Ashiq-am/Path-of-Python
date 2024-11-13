""



"""

// Some Python Object
PyObject *obj;

// Conversion from bytes
{
	char *s;
	s = PyBytes_AsString(o);
	if (!s)
	{
		/* TypeError already raised */
		return NULL;
	}
	print_chars(s);
}




"""