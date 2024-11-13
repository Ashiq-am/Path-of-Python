""



"""

# include "Python.h"
# include "sample.h"

/* int gcd(int, int) */
static PyObject * py_gcd(PyObject * self, PyObject * args)
{
	int x, y, result;
	if (! PyArg_ParseTuple(args, "ii", &x, &y))
	{
		return NULL;
	}
	result = gcd(x, y);
	return Py_BuildValue("i", result);
}

/* int divide(int, int, int *) */
static PyObject * py_divide(PyObject * self, PyObject * args)
{
	int a, b, quotient, remainder;
	if (! PyArg_ParseTuple(args, "ii", &a, &b))
	{
		return NULL;
	}
	quotient = divide(a, b, &remainder);
	return Py_BuildValue("(ii)", quotient, remainder);
}



"""