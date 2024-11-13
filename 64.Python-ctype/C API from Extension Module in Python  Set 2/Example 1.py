""


'''

#include "pythonsample.h"
/* An extension function that uses the exported API */
static PyObject *print_point(PyObject *self, PyObject *args)
{
	PyObject *obj;
	Point *p;
	if (!PyArg_ParseTuple(args, "O", &obj))
	{
		return NULL;
	}
	/* Note: This is defined in a different module */
	p = PyPoint_AsPoint(obj);
	if (!p)
	{
		return NULL;
	}
	printf("%f %f\n", p->x, p->y);
	return Py_BuildValue("");
}

static PyMethodDef PtExampleMethods[] =
{
	{"print_point", print_point, METH_VARARGS, "output a point"},
	{ NULL, NULL, 0, NULL}
};

static struct PyModuleDef ptexamplemodule =
{
	PyModuleDef_HEAD_INIT,
	/* name of module */
	"ptexample",
	/* Doc string (may be NULL) */
	"A module that imports an API",
	/* Size of per-interpreter state or -1 */
	-1,
	/* Method table */
	PtExampleMethods
	
};


'''