""



"""
/* Turn a filename into a Python object */
char* filename;
int filename_len;
PyObject* obj = PyUnicode_DecodeFSDefaultAndSize(
	filename, filename_len);



"""