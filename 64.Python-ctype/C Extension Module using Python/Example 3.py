""


'''

/* Module method table */
static PyMethodDef SampleMethods[] =
{
	{"gcd", py_gcd, METH_VARARGS, "Greatest common divisor"},
	{"divide", py_divide, METH_VARARGS, "Integer division"},
	{ NULL, NULL, 0, NULL}
};

/* Module structure */
static struct PyModuleDef samplemodule =
{
	PyModuleDef_HEAD_INIT,
	"sample", /* name of module */
	"A sample module", /* Doc string (may be NULL) */
	-1, /* Size of per-interpreter state or -1 */
	SampleMethods /* Method table */
};

/* Module initialization function */
PyMODINIT_FUNC
PyInit_sample(void)
{
	return PyModule_Create(&samplemodule);
}



'''